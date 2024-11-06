@echo off
rem 启动 SSH 代理
eval $(ssh-agent -s)
rem 添加 SSH 私钥
ssh-add C:/Users/admin/Desktop/rep_for_gitub/ssh/id_rsa

rem 添加更改到 Git 仓库
git add .

rem 提交更改
git commit -m "Your commit message"

rem 推送更改到远程仓库
git push -u origin master

rem 完成操作
echo Git push 完成
pause
