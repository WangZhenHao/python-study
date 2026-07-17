## 激活环境

mac: source venv/bin/activate
windows: venv\Scripts\activate

退出

deactivate

# 1. 查看所有可安装的 Python 版本
pyenv install --list

# 2. 安装你需要的版本，例如 3.10.0
pyenv install 3.10.0

# 3. 切换版本
#    全局切换 (整个系统生效)
pyenv global 3.10.0

#    项目级切换 (在当前目录生效，会生成一个 .python-version 文件)
pyenv local 3.10.0

安装uv 包管理

curl -LsSf https://astral.sh/uv/install.sh | sh

source ~/.zshrc

创建项目时指定版本
uv init --python 3.14