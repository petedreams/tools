#!/usr/bin/env python
# -*- coding: utf-8 -*-



import os,sys,dpkt,socket,binascii,string,re, operator,socket,datetime,time,struct
def header(file):

    f= open(file)
    pcap = dpkt.pcap.Reader(f)

    for ts,buf in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
        except:
            continue

        if type(eth.data) == dpkt.ip.IP:
            ip = eth.data
            src_addr=socket.inet_ntoa(ip.src)
            dst_addr=socket.inet_ntoa(ip.dst)

            if type(ip.data) == dpkt.udp.UDP:
                udp = ip.data
                if udp.sport == 53 or udp.dport == 53:
                    try:
                        dns = dpkt.dns.DNS(udp.data)
                        ipid = struct.unpack(">H",struct.pack("<H",ip.id))
                        dnsid = struct.unpack(">H",struct.pack("<H",dns.id))
                        if dnsid[0]==ipid[0]&0x2345:
                            #print ipid%4996+1400 
                            if udp.sport==(ipid[0]%4996+1400) or udp.dport==(ipid[0]%4996+1400):
                                print src_addr
                        #print "%x"%(ipid[0]&0x2345)
                        #print "%x -> %x"%(dns.id,dnsid[0])

                        
                        #print "ipid:%x, dnsid:%d"%(ip.id,dns.id)
                        #print "dnsid & 0x2345: %d" %(dns.id & 0x2345)
                        #print dns.id&0x2345
                    except:
                        pass

if __name__ == '__main__':
    filename = sys.argv[1]
    if "/" in filename:
        infile =  filename[filename.rindex('/')+1:]
    else :
        infile = filename
    print infile
    header(filename)
