import subprocess
import os

# 启动 SSH agent 并返回环境变量
def start_ssh_agent():
    result = subprocess.run(['ssh-agent', '-s'], capture_output=True, text=True)
    if result.returncode == 0:
        # 解析环境变量
        for line in result.stdout.splitlines():
            if "SSH_AGENT_PID" in line:
                pid = line.split('=')[1].strip()
                os.environ["SSH_AGENT_PID"] = pid
            if "SSH_AUTH_SOCK" in line:
                sock = line.split('=')[1].strip()
                os.environ["SSH_AUTH_SOCK"] = sock
        print("SSH agent started.")
        return True
    else:
        print("Failed to start SSH agent.")
        return False

# 添加 SSH 密钥到 agent
def add_ssh_key_to_agent(private_key_path):
    result = subprocess.run(['ssh-add', private_key_path], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"Successfully added {private_key_path} to SSH agent.")
    else:
        print(f"Failed to add {private_key_path} to SSH agent. Error: {result.stderr}")

# 执行 Git 命令
def git_commit_and_push(commit_message):
    # 使用 Git 命令
    commands = [
        ['git', 'add', '.'],
        ['git', 'commit', '-m', commit_message],
        ['git', 'push', '-u', 'origin', 'master']
    ]
    
    for command in commands:
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Successfully executed: {' '.join(command)}")
            print(result.stdout)
        else:
            print(f"Failed to execute: {' '.join(command)}")
            print(result.stderr)
            break

# 自动化执行的流程
if __name__ == "__main__":
    private_key_path = "C:/Users/admin/Desktop/rep_for_gitub/ssh/id_rsa"
    commit_message = "Your commit message"
    
    # 启动 SSH agent 并添加密钥
    if start_ssh_agent():
        add_ssh_key_to_agent(private_key_path)
    
    # 执行 Git 提交和推送操作
    git_commit_and_push(commit_message)
