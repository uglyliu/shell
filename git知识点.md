##git重要命令操作

###撤销修改
    git checkout -- filename

###git checkout小结
    场景1：当你改乱了工作区某个文件的内容，想直接丢弃工作区的修改时，用命令git checkout -- file
    
    场景2：当你不但改乱了工作区某个文件的内容，还添加到了暂存区时，想丢弃修改，分两步，第一步命令git reset HEAD file,就回到了场景1，第二步按场景1操作
###git鼓励大量使用分支
    查看分支 git branch
    创建分支 git branch <name>
    切换分支 git checkout <name>
    创建+切换分支 git checkout -b <name>
    合并某分支到当前分支 git merge <name>
    删除分支 git branch -d <name>
###Git冲突
    git log --graph命令可以看到分支合并图
    git log --graph --pretty=oneline --abbrev-commit  #用带参数的git log也可以看到分支的合并情况
    git merge --no-ff -m "merge with no-off" dev #使用--no-ff参数就可以用普通模式合并，合并后的历史有分支，能看出来曾经做过合并，而fast forward合并就看不出来曾经做过合并
###bug分支

    修复bug时，我们会通过创建新的bug分支进行修复，然后合并，最后删除
    当手头工作没有完成，先把工作现场git stash一下，然后去修复bug，修复后，再git stash pop，回到工作现场

###Features分支
    开发一个新feature，，最好新建一个分支
    如果要丢弃一个没有被合并过的分支，可以通过git branch -D <name>强行删除   

###多人合作
    查看远程库信息，使用git remote -v；

    本地新建的分支如果不推送到远程，对其他人就是不可见的；

    从本地推送分支，使用git push origin branch-name，如果推送失败，先用git pull抓取远程的新提交；

    在本地创建和远程分支对应的分支，使用git checkout -b branch-name origin/branch-name，本地和远程分支的名称最好一致；

    建立本地分支和远程分支的关联，使用git branch --set-upstream branch-name origin/branch-name；

    从远程抓取分支，使用git pull，如果有冲突，要先处理冲突。
