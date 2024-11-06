# 启动 SSH 代理
Start-Process "ssh-agent" -ArgumentList "-s" -Wait

# 添加 SSH 密钥到 SSH 代理
ssh-add "C:/Users/admin/Desktop/rep_for_gitub/ssh/id_rsa"

# 添加所有更改到 Git 仓库
git add .

# 提交更改
git commit -m "Your commit message"

# 推送到远程仓库
git push -u origin master

# 输出完成信息
Write-Host "Git push 完成"
