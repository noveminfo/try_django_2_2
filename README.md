# try_django_2_2

# local

git init

git add *

git remote add origin https://github.com/noveminfo/try_django_2_2.git

git commit -m "try_django"

git push origin master
>>error: failed to push some refs to 'https://github.com/noveminfo/try_django_2_2.git'
>>hint: Updates were rejected because the remote contains work that you do
>>hint: not have locally. This is usually caused by another repository pushing
>>hint: to the same ref. You may want to first integrate the remote changes
>>hint: (e.g., 'git pull ...') before pushing again.
>>hint: See the 'Note about fast-forwards' in 'git push --help' for details.

git merge --allow-unrelated-histories origin/master

git push origin master