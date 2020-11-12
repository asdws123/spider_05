# GIT使用流程

帐号：asdws123

mima:18437912007zjl

1. linux安装GIT

   ​	`sudo apt install git`

2. 初始配置

   配置命令： git config --global [选项]

   配置文件位置:  ~/.gitconfig

   配置用户名：sudo git config --global user.name xxx

   配置用户邮箱:git config --global user.email xxx

   查看配置信息:git config --list

3. 初始化仓库--生成本地仓库

   `git  init`

   注：在哪个文件夹下执行该命令，该文件夹就成为git本地仓库

4. 查看本地仓库状态

   `git  status`

   默认工作在master分支

   未跟踪文件：在工作区未在暂存区中的项目文件

5. 将工作内容记录到暂存区

   `git add [file]`                   注：*表示所有文件

6. 取消文件暂存记录

   `git rm --cached [file] `
   `git rm --cached  -r  [dir]`

7. 设置忽略文件

   先设置忽略文件：在项目根目录添加.gitignore文件

   在.gitignore文件中添加要忽略的文件，规则如下：

   ```
   file            表示忽略file文件
   *.a             表示忽略所有 .a 结尾的文件
   !lib.a          表示但lib.a除外
   build/          表示忽略 build/目录下的所有文件，过滤整个build文件夹；
   ```

8. 将暂存区文件同步到本地仓库

   `git commit  [file] -m [message]`
   说明: -m表示添加一些同步信息，表达同步内容,不加file表示同步所有暂存记录的文件

9. 查看commit 日志记录

   `git log`                   #查看commit 提交到仓库的日志记录

10. 将暂存区或者某个commit点文件恢复到工作区

    `git checkout [commit] -- [file]`

    e.g. 将a.jpg文件恢复,不写commit表示恢复最新保存的文件内容

11. 移动或者删除文件

    `git  mv  [file] [path] `    

    `git  rm  [files]#将本地文件先删除`

    注意: 这两个操作会修改工作区内容，同时将操作记录提交到暂存区。
    `git  commit -m 'rm [files]'`#将仓库中同名文件也删除

12. 退回到上一个commit节点

    `git reset --hard HEAD^`

    说明： 一个^表示回退1个版本

13. 退回到指定的commit_id节点

      `git reset --hard [commit_id]`

14. 查看所有操作记录

      `git reflog`

15. 创建标签

    `git  tag  [tag_name] [commit_id] -m  [message]`

    标签: 在项目的重要commit位置添加快照，保存当时的工作状态，一般用于版本的迭代。

    commit_id可以不写则默认标签表示最新的commit_id位置

16. 查看标签

     `git tag  查看标签列表`
     `git show [tag_name]  查看标签详细信息`

17. 去往某个标签节点

    `git reset --hard [tag]`

18. 删除标签

    `git tag -d  [tag]`

19. 保存工作区内容

    `git stash save [message]`
    说明: 将工作区未提交的修改封存，让工作区回到修改前的状态
    可以进行新的修改而不影响之前的修改

20. 查看工作区列表

    `git stash  list`

    说明:最新保存的工作区在最上面

21. 应用某个工作区

    `git stash  apply   [stash@{n}]`

22. 删除工作区

    `git stash drop [stash@{n}]`  删除某一个工作区
    `git stash clear`  删除所有保存的工作区

23. 查看现有分支

    `git branch`
    说明: 前面带 * 的分支表示当前工作分支

24. 创建分支

    `git branch [branch_name]`
    说明: 基于a分支创建b分支，此时b分支会拥有a分支全部内容。在创建b分支时最好保持a分支"干净"状态。

25. 切换工作分支

    `git checkout [branch]`
    说明: 2,3可以同时操作，即创建并切换分支

26. 合并分支

    `git merge [branch]`

    注意：分支的合并一般都是子分支向父分支中合并

27. 删除分支

    ` git branch -d [branch]`  删除分支
     `git branch -D [branch] ` 删除没有被合并的分支



# GitHub使用

1. 先在github上创建一个新的仓库

2. 网址：https://github.com/

3. 下载别人的git库

   `git clone https://github.com/xxxxxxxxx`

4. 链接自己的github

   ·使用https链接

   `git remote  add origin https://github.com/xxxxxxxxx`  --麻烦，临时

   ·使用SSH连接

    先建立秘钥:

   将自己要连接github的计算机的ssh公钥内容复制

   github上选择头像下拉菜单，settings->SSH and GPG keys->new SSH key

   将公钥内容添加进去，并且起一个标题名字，点击添加

   `git remote add origin git@github.com:asdws123/xxx.git`   --安全

5. 查看连接的远程仓库名称

   `git remote`

6. 断开远程仓库连接

   `git remote rm [origin]`

7. 删除自己仓库

   选择自己的仓库选择settings，在最后可以选择删除仓库。

8. 将本地分支推送给远程仓库

   将master分支推送给origin主机远程仓库，第一次推送分支使用-u表示与远程对应分支	建立自动关联

   `git push -u origin  master`

9. 删除远程仓库的分支

   `git push origin  [:branch]`

10. 推送代码到远程仓库

   当前工作区文件上传本地库后才能上传远程仓库

   如果本地的代码有修改项推送给远程仓库

   `git push`

11. 推送标签

    `git push origin [tag]`  推送一个本地标签到远程

    `git push origin --tags`  推送所有本地所有标签到远程

    `git push origin --delete tag  [tagname]`  删除远程仓库的标签

12. 推送旧的版本

    用于本地版本比远程版本旧时强行推送本地版本

    git push --force origin  

13. 从远程获取代码

    `git pull`

    

    

    # 码云：gitee

    asdws123

    18437912007zjl

    说明：管理github代码

    

    

    