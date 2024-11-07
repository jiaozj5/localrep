#!/bin/bash

conda activate dl
python C:\\Users\\admin\\Desktop\\rep2_for github\\git_push.py

# 启动 SSH 代理
eval $(ssh-agent -s)

# 添加 SSH 密钥
ssh-add C:/Users/admin/Desktop/rep_for_gitub/ssh/id_rsa

# 添加更改到 Git 仓库
git add .

# 提交更改
git commit -m "Your commit message"

# 推送更改到远程仓库
git push -u origin master

# 输出完成信息
echo "Git push 完成"


