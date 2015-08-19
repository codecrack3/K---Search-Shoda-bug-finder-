#-------------------------------------------------------------------------------
# Name:        k-search
# Purpose:
#
# Author:      kai - ceh.vn
#
# Created:    9h45 PM -  19/08/2015
# Copyright:   (c) kai 2015
#
#-------------------------------------------------------------------------------

try:
        import shodan
except:
        print "Not lib shodan install now "
import sys
import os
import socket

API_KEY = "ss7HcLsHc6ZqOtT71LFpVAblP5OUTCfD"


def searchexploit(text):
        try:
                api = shodan.Shodan(API_KEY)
                query = ' '.join(sys.argv[1:])
                result = api.exploits.search(query)
                count = api.exploits.count(query)
                for service in result['matches']:
                        try:
                                print "Author: %s" % service['author']
                        except:
                                continue
                        print "ID: %s " % service['_id']
                        print "Des: %s " % service['description']
                        print "Source: %s " % service['source']
                        if service['source'] == "ExploitDB":
                                saveexploit("Des: %s " % service['description'] + "Link Exploit: http://www.exploit-db.com/exploits/%s/" % str(service['_id'])+'\n')
                                print "Link Exploit: http://www.exploit-db.com/exploits/%s/" % service['_id']
                        elif service['source'] == "Metasploit":
                                saveexploit("Des: Metasploit: %s" % str(service['_id'])+'\n')
                                print "link : %s" % service['_id']
                        print "-"*70
                #try:
                        #print service['code']
                #except:
                        #continue
        except Exception, e:
                print 'Error Found :( : %s' % e
                sys.exit(1)

def saveexploit(log):
        f = open('log.txt','a+')
        f.write(log)
        f.close()
        
if __name__ == "__main__":
        if len(sys.argv) == 1:
                print '-'*50
                print 'Exploit Database Finder :q\nCode: Kai (ceh.vn) \n'
                print 'Usage: %s <search text query>' % sys.argv[0]
                print '-'*50
                sys.exit(1)
        else:
                searchexploit(sys.argv[1:])
		os.system(['cat log.txt','log.txt'][os.name == 'nt'])
		os.remove('log.txt')
                
                
