#!/usr/bin/env pwsh

$BazelDockerImageUrl = "gcr.io/cloud-builders/bazel"

function Test-Docker-Availability {
    if (![bool](Get-Command -Name "docker" -ErrorAction SilentlyContinue)) {
        Write-Host "[ERROR]: Unable to find docker in your system. Did you installed it ?"
        exit 1
    }
}

function Test-Bazel-Availability {
    # If bazel is defined as a Powershell Item (not a binary itself) remove
    # it and, if required, the function will re-create it at the very end.
    if (Test-Path Function:bazel) { Remove-Item Function:bazel }
    if (![bool](Get-Command -Name "bazel" -ErrorAction SilentlyContinue)) {
        $DockerCmd = Get-Command docker | Select-Object -ExpandProperty Definition | Out-String -NoNewline
        $GetImageCmd = ("{0} images {1} -q" -f $DockerCmd, $BazelDockerImageUrl)
        $ImageId = Invoke-Expression $GetImageCmd | Out-String -NoNewline
        if (!$ImageId) {
            $CreateImageCmd = ("{0} pull {1}" -f $DockerCmd, $BazelDockerImageUrl)
            Invoke-Expression $CreateImageCmd
            $ImageId = Invoke-Expression $GetImageCmd | Out-String -NoNewline
        }
        Set-Item -Path Function:global:bazel -Value { 
            $DockerCmd = Get-Command docker | Select-Object -ExpandProperty Definition | Out-String -NoNewline
            $GetImageCmd = ("{0} images {1} -q" -f $DockerCmd, $BazelDockerImageUrl)
            $ImageId = Invoke-Expression $GetImageCmd | Out-String -NoNewline
            $BazelCmd = ("{0} run --rm -it -v {1}:/workspace -w /workspace {2} $args" `
                -f $DockerCmd, $PSScriptRoot, $ImageId)
            Invoke-Expression $BazelCmd
        }
    }
}

Test-Docker-Availability
Test-Bazel-Availability

# Unset helper functions + variables to prevent them from showing up on SHELL auto-complete.
Remove-Item -Path Function:Test-Docker-Availability
Remove-Item -Path Function:Test-Bazel-Availability