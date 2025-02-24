A project to processed lambwave receievd from your sensors.

git init #初始化
~/.ssh
ssh -T git@github.com
# ssh-keygen -t -rsa -C "YOUR MAIL" （3 times ENTER）

# 完整上传本地已有项目
git remote add main git@github.com:QL1009/lambwave_processing.git # 建立连接关系
git remote -v # 检查连接状态
git branch -M master # 修改本地分支名称
git push -u master main # 上传

# 修改项目并上传
git add .  # 添加所有文件到暂存区
git commit -m '提交的文字描述'  # 从暂存区提交
git pull main main    # 拉取最新状态到本地
git push main main  # 推送到远程仓库

git status  # 查看当前分支修改的文件
git branch A  # 创建分支 A
git checkout A  # 切换分支到 A
git branch -D A  # 删除本地分支 A
git diff  # 查询当前分支代码与远程代码仓库的区别
git log  # 查看提交记录（找到要回滚的版本号）
git reset --hard '版本号'  # 执行回滚操作
git checkout .  # 撤销所有修改
git checkout tcms/handlers.py  # 撤销单个文件修改
git remote -v # 检查连接状态


#一般修改流程
git status  # 查看当前分支修改的文件
git add .  # 添加所有文件到暂存区
git commit -m '提交的文字描述'  # 从暂存区提交
git pull main main    # 拉取最新状态到本地
git push main main  # 推送到远程仓库
