@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

:: MCP Hub Windows 一键安装脚本
:: =============================

echo.
echo ╔══════════════════════════════════════════════════════════════╗
echo ║                    🚀 MCP Hub 自动安装器                      ║
echo ║              Standalone Model Context Protocol              ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.

:: 检查Python
echo 🔧 检查Python环境...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python未安装，请先安装Python 3.8+
    echo 下载地址: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo ✅ Python已安装

:: 检查pip
echo 🔧 检查pip...
pip --version >nul 2>&1
if errorlevel 1 (
    echo ❌ pip未安装
    pause
    exit /b 1
)

echo ✅ pip已安装

:: 创建虚拟环境
echo.
echo 📦 创建虚拟环境...
if not exist "venv" (
    python -m venv venv
    echo ✅ 虚拟环境创建成功
) else (
    echo ✅ 虚拟环境已存在
)

:: 激活虚拟环境并安装依赖
echo.
echo 📦 安装依赖包...
call venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt
echo ✅ 依赖安装完成

:: 创建启动脚本
echo.
echo 🔧 创建启动脚本...

:: 通用启动脚本
echo @echo off > start_mcp.bat
echo call venv\Scripts\activate.bat >> start_mcp.bat
echo python mcp_hub.py %%* >> start_mcp.bat

:: AI模式启动脚本
echo @echo off > start_ai.bat
echo call venv\Scripts\activate.bat >> start_ai.bat
echo python mcp_hub.py --mode=ai >> start_ai.bat

:: 笔记模式启动脚本
echo @echo off > start_notes.bat
echo call venv\Scripts\activate.bat >> start_notes.bat
echo python mcp_hub.py --mode=notes >> start_notes.bat

:: 写作模式启动脚本
echo @echo off > start_writing.bat
echo call venv\Scripts\activate.bat >> start_writing.bat
echo python mcp_hub.py --mode=writing >> start_writing.bat

:: 工程模式启动脚本
echo @echo off > start_engineering.bat
echo call venv\Scripts\activate.bat >> start_engineering.bat
echo python mcp_hub.py --mode=engineering >> start_engineering.bat

:: 实验模式启动脚本
echo @echo off > start_experiment.bat
echo call venv\Scripts\activate.bat >> start_experiment.bat
echo python mcp_hub.py --mode=experiment >> start_experiment.bat

echo ✅ 启动脚本创建成功

:: 创建一键启动脚本
echo @echo off > one_click.bat
echo chcp 65001 ^>nul >> one_click.bat
echo echo. >> one_click.bat
echo echo ╔══════════════════════════════════════════════════════════════╗ >> one_click.bat
echo echo ║                    🚀 MCP Hub 一键启动                       ║ >> one_click.bat
echo echo ║                    简单易用，一键搞定！                       ║ >> one_click.bat
echo echo ╚══════════════════════════════════════════════════════════════╝ >> one_click.bat
echo echo. >> one_click.bat
echo echo 🎯 请选择MCP Hub模式: >> one_click.bat
echo echo 1^) 🔬 AI研究模式 ^(Ray + Dask + OpenAI^) >> one_click.bat
echo echo 2^) 📚 笔记模式 ^(Obsidian + Zotero^) >> one_click.bat
echo echo 3^) 💬 写作模式 ^(LangChain + LangGraph^) >> one_click.bat
echo echo 4^) 🧪 工程模式 ^(Simulink + Python^) >> one_click.bat
echo echo 5^) 🧭 实验模式 ^(FastAPI + GitHub^) >> one_click.bat
echo echo 6^) 🎭 演示模式 ^(查看所有模式^) >> one_click.bat
echo echo 7^) ❓ 帮助信息 >> one_click.bat
echo echo. >> one_click.bat
echo set /p choice=请输入选择 ^(1-7^):  >> one_click.bat
echo if "%%choice%%"=="1" start_ai.bat >> one_click.bat
echo if "%%choice%%"=="2" start_notes.bat >> one_click.bat
echo if "%%choice%%"=="3" start_writing.bat >> one_click.bat
echo if "%%choice%%"=="4" start_engineering.bat >> one_click.bat
echo if "%%choice%%"=="5" start_experiment.bat >> one_click.bat
echo if "%%choice%%"=="6" ^(call venv\Scripts\activate.bat ^&^& python demo.py^) >> one_click.bat
echo if "%%choice%%"=="7" ^(call venv\Scripts\activate.bat ^&^& python mcp_hub.py --help^) >> one_click.bat

echo ✅ 一键启动脚本创建成功

:: 显示完成信息
echo.
echo 🎉 MCP Hub 安装成功！
echo.
echo 📖 使用方法:
echo   start_mcp.bat --mode=ai          # 启动AI研究模式
echo   start_mcp.bat --mode=notes       # 启动笔记模式
echo   start_mcp.bat --mode=writing     # 启动写作模式
echo.
echo ⚡ 快速启动:
echo   start_ai.bat                     # 直接启动AI模式
echo   start_notes.bat                  # 直接启动笔记模式
echo   start_writing.bat                # 直接启动写作模式
echo.
echo 🚀 一键启动:
echo   one_click.bat                    # 交互式选择模式
echo.
echo 📚 更多信息:
echo   type README.md                   # 查看详细文档
echo.
pause
