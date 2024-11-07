#!/bin/bash

conda init bash
conda activate dl
python "C:\\Users\\admin\\Desktop\\rep2_for github\\git_push.py"

sleep 20

# 启动 SSH 代理
eval $(ssh-agent -s)

# 添加 SSH 密钥
ssh-add C:/Users/admin/Desktop/rep_for_gitub/ssh/id_rsa

# 添加更改到 Git 仓库
git add .

# 提交更改
git commit -m "Your commit message"

# 强制推送更改到远程仓库，覆盖 GitHub 上的 master 分支
git push -u origin master --force

# 输出完成信息
echo "Git push 完成"

sleep 30
