@echo off

echo ========================================
echo Running pytest...
echo ========================================

pytest

IF %ERRORLEVEL% NEQ 0 (
    echo Pytest failed.
    exit /b %ERRORLEVEL%
)

echo.
echo ========================================
echo Building Docker image...
echo ========================================

docker build -t netflix-pipeline .

IF %ERRORLEVEL% NEQ 0 (
    echo Docker build failed.
    exit /b %ERRORLEVEL%
)

echo.
echo ========================================
echo Running Docker container...
echo ========================================

docker run --rm netflix-pipeline

IF %ERRORLEVEL% NEQ 0 (
    echo Docker run failed.
    exit /b %ERRORLEVEL%
)

echo.
echo ========================================
echo Pipeline completed successfully!
echo ========================================