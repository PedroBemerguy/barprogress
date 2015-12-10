import argparse
import time
import os
import sys
import threading
import multiprocessing
import signal


class bar_class():

    def bar(self,loader,bar_progress_l,bar_empty_l,g_l,time_total):
        time_init_load=time.time()
        sys.stdout.write("\r[%s%s%s] Current Gain:%f / Time running: %f "%\
                                           (bar_progress_l,bar_empty_l,loader,g_l,time_total))
        sys.stdout.flush();
        time.sleep(0.05)


    def loader(self,bar_progress_p,bar_empty_p,g_p,time_trans):
          while True:
            for i in range(1,5):
                # if i == 1:
                #     bar('-',bar_progress_p,bar_empty_p,g_p,time_trans)
                # elif i == 2:
                #     bar('/',bar_progress_p,bar_empty_p,g_p,time_trans)
                # elif i == 3:
                #     bar('|',bar_progress_p,bar_empty_p,g_p,time_trans)
                # else:
                #     bar('\\',bar_progress_p,bar_empty_p,g_p,time_trans)
                dict = {
                      1: self.bar('-',bar_progress_p,bar_empty_p,g_p,time_trans),
                      2: self.bar('/',bar_progress_p,bar_empty_p,g_p,time_trans),
                      3: self.bar('|',bar_progress_p,bar_empty_p,g_p,time_trans),
                      4: self.bar('\\',bar_progress_p,bar_empty_p,g_p,time_trans)
                }

    

      


parser = argparse.ArgumentParser()
parser.add_argument('-g', '--gain', nargs=2, type=int, required=True,\
                    help='apaala')
args = parser.parse_args()


if args.gain[0] > args.gain[1]:
    i = -1
elif args.gain[0] < args.gain[1]:
    i = 1
else:
    print "The gain need to have different values"
    sys.exit()
gain_list=range(args.gain[0],args.gain[1]+i,i)

print gain_list


if __name__ == '__main__':
    if (i == -1):
        try:
          time_init=time.time()
          m_bar_class = bar_class()
          for g in gain_list:
                bar_progress = ((args.gain[0]-g)*'#')
                bar_empty = ' '*(g-args.gain[1])
                p = multiprocessing.Process(target=m_bar_class.loader,args=(bar_progress,bar_empty,g,time.time()-time_init,))
                p.start()
                time.sleep(1.2)
                p.terminate()
        except [[KeyboardInterrupt]]:
            pass 
        
        sys.stdout.write("\r[%s%s] Current Gain:%f / Time running: %f \n"%\
                                ('#'*(args.gain[0]-args.gain[1]-i),' '*0,g,time.time()-time_init))
    else:
        try:
          time_init=time.time()
          for g in gain_list:
                bar_progress =(g-args.gain[0])*'#'
                bar_empty = ' '*(args.gain[1]-g)
                p = multiprocessing.Process(target=m_bar_class.loader,args=(bar_progress,bar_empty,g,time.time()-time_init,))
                p.start()
                time.sleep(1.2)
                p.terminate()
        except [[KeyboardInterrupt]]:
            pass
        sys.stdout.write("\r[%s%s] Current Gain:%f / Time running: %f \n"%\
                                ('#'*(args.gain[1]-args.gain[0]+i),' '*0,g,time.time()-time_init))
