# coding: utf-8
#JS_TEMPLATE_PATH  = 'templates/js.html.tt'
#CSS_TEMPLATE_PATH = 'templates/css.html.tt'
#MNG_CSS_TEMPLATE_PATH = 'templates/mng/css.html.tt'
# all ==============================================================================================

task :default do
    system 'rake -T'
end

# pull =============================================================================================

desc "pull all"
task :all_pull => :origin_pull do
    sh 'git pull bit master'
    sh 'git pull github master'
end

desc "pull origin"
task :origin_pull do
    sh 'git pull origin master'
end

desc "pull bitbucket"
task :bit_pull do
    sh 'git pull bit master'
end

desc "pull github"
task :github_pull do
    sh 'git pull github master'
end

# push =============================================================================================

desc "push all"
task :all_push => :all_pull do
    sh 'git push origin master'
    sh 'git push bit master'
    sh 'git push github master'
end

desc "push origin"
task :push => :origin_pull do
    sh 'git push origin master'
end

desc "push bitbucket"
task :bit_push => :bit_pull do
    sh 'git push bit master'
end

desc "push github"
task :github_push => :github_pull do
    sh 'git push github master'
end

# "всякая муйня по рейку http://www.opennet.ru/base/dev/rake_rails.txt.html"
#EOF
