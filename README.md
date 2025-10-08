# MCP Hub - 模型上下文协议中心

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![MCP](https://img.shields.io/badge/MCP-Protocol-orange.svg)](https://modelcontextprotocol.io)

一个强大的本地MCP（模型上下文协议）协调中心，支持多种AI工具的无缝集成。

## 🚀 快速开始

### 一键安装（推荐）

**Linux/macOS:**
```bash
sudo ./one_click.sh
```

**Windows:**
```cmd
install.bat
```

**Docker:**
```bash
sudo ./docker_start.sh
```

### 手动安装

1. **克隆项目**
```bash
git clone https://github.com/yourusername/MCP_Terminal.git
cd MCP_Terminal
```

2. **安装依赖**
```bash
sudo ./install.sh
```

3. **运行**
```bash
python mcp_hub.py --mode=ai
```

## 🎯 支持的模式

| 模式 | 命令 | 描述 | 工具组合 |
|------|------|------|----------|
| AI研究 | `--mode=ai` | 数据科学和AI研究 | Ray + Dask + OpenAI |
| 工程开发 | `--mode=engineering` | 软件工程和开发 | LangChain + LangGraph + FastAPI |
| 实验测试 | `--mode=experiment` | 实验和测试 | Ray + Dask + Requests |
| MCP工具 | `--mode=mcp` | 通用MCP工具 | 所有工具 |
| 笔记管理 | `--mode=notes` | 笔记和文档 | Obsidian + 文件系统 |
| 写作助手 | `--mode=writing` | 写作和编辑 | OpenAI + 文件系统 |

## 🔧 API使用指南

### 连接成功后，您可以使用以下API：

#### 1. Ray API - 分布式计算
```python
# 启动Ray集群
ray.init()

# 创建远程函数
@ray.remote
def process_data(data):
    return data * 2

# 并行处理
futures = [process_data.remote(i) for i in range(10)]
results = ray.get(futures)

# 关闭Ray
ray.shutdown()
```

#### 2. Dask API - 大数据处理
```python
import dask.array as da

# 创建大型数组
x = da.random.random((10000, 10000), chunks=(1000, 1000))

# 并行计算
result = (x + x.T).sum()

# 执行计算
result.compute()
```

#### 3. OpenAI API - AI服务
```python
import openai

# 设置API密钥
openai.api_key = "your-api-key"

# 文本生成
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello!"}]
)

print(response.choices[0].message.content)
```

#### 4. LangChain API - 语言模型链
```python
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# 创建语言模型
llm = OpenAI(temperature=0.7)

# 创建提示模板
prompt = PromptTemplate(
    input_variables=["topic"],
    template="请写一篇关于{topic}的文章"
)

# 创建链
chain = LLMChain(llm=llm, prompt=prompt)

# 运行链
result = chain.run("人工智能")
```

#### 5. LangGraph API - 图工作流
```python
from langgraph import StateGraph, END

# 定义状态
class WorkflowState(TypedDict):
    input: str
    processed: str
    output: str

# 创建节点
def process_node(state: WorkflowState):
    return {"processed": state["input"].upper()}

def output_node(state: WorkflowState):
    return {"output": f"结果: {state['processed']}"}

# 构建图
workflow = StateGraph(WorkflowState)
workflow.add_node("process", process_node)
workflow.add_node("output", output_node)
workflow.add_edge("process", "output")
workflow.add_edge("output", END)

# 编译并运行
app = workflow.compile()
result = app.invoke({"input": "hello world"})
```

#### 6. FastAPI API - Web服务
```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.post("/items/")
async def create_item(item: Item):
    return {"message": f"创建了 {item.name}，价格 {item.price}"}

@app.get("/")
async def root():
    return {"message": "Hello World"}

# 运行: uvicorn main:app --reload
```

#### 7. Obsidian API - 笔记管理
```python
import os
import json

# 读取笔记
def read_note(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

# 创建笔记
def create_note(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

# 搜索笔记
def search_notes(directory, keyword):
    results = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                content = read_note(file_path)
                if keyword in content:
                    results.append(file_path)
    return results
```

## 🛠️ 交互式命令

连接成功后，您可以使用以下命令：

- `help` - 显示所有可用命令
- `status` - 显示工具连接状态
- `tools` - 列出所有可用工具
- `mode` - 显示当前模式
- `switch <mode>` - 切换模式
- `demo` - 运行演示
- `quit` - 退出程序

## 📁 项目结构

```
MCP_Terminal/
├── mcp_hub.py          # 主程序
├── tools/              # MCP工具模块
│   ├── __init__.py
│   ├── ray_mcp.py      # Ray工具
│   ├── dask_mcp.py     # Dask工具
│   ├── openai_mcp.py   # OpenAI工具
│   ├── langchain_mcp.py # LangChain工具
│   └── obsidian_mcp.py # Obsidian工具
├── requirements.txt    # 依赖列表
├── config.json        # 配置文件
├── install.sh         # Linux/macOS安装脚本
├── install.bat        # Windows安装脚本
├── one_click.sh       # 一键启动脚本
├── docker_start.sh    # Docker启动脚本
├── cleanup.sh         # 清理脚本
└── start_*.sh         # 各模式启动脚本
```

## 🔧 配置

### 环境变量
```bash
# OpenAI API密钥
export OPENAI_API_KEY="your-openai-api-key"

# 其他API密钥
export RAY_ADDRESS="ray://localhost:10001"
export DASK_SCHEDULER="tcp://localhost:8786"
```

### 配置文件
编辑 `config.json` 来自定义工具配置：

```json
{
  "modes": {
    "ai": {
      "tools": ["ray", "dask", "openai"],
      "description": "数据科学和AI研究"
    }
  }
}
```

## 🐛 故障排除

### 常见问题

1. **依赖安装失败**
   ```bash
   sudo pip install --upgrade pip
   sudo ./install.sh
   ```

2. **权限问题**
   ```bash
   chmod +x *.sh
   sudo ./one_click.sh
   ```

3. **端口冲突**
   - 检查端口占用：`lsof -i :8000`
   - 修改配置文件中的端口设置

4. **API密钥问题**
   ```bash
   ./setup_env.sh
   ```

### 日志查看
```bash
tail -f mcp_hub.log
```

## 🤝 贡献

欢迎提交Issue和Pull Request！

1. Fork项目
2. 创建功能分支
3. 提交更改
4. 推送到分支
5. 创建Pull Request

## 📄 许可证

MIT License - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🙏 致谢

感谢所有MCP工具的开发者和社区贡献者！

---

**开始使用MCP Hub，让AI工具协同工作！** 🚀