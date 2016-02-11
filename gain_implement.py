import argparse
import time
import os
import sys
import threading
import multiprocessing
import signal


class bar_class():

    def bar(self, loader, bar_progress_l, bar_empty_l, g_l, time_total):    
        sys.stdout.write("\r[%s%s%s] Current Gain: %f / Time running: %0.3f "%\
                        (bar_progress_l, bar_empty_l, loader,g_l, time_total))
        sys.stdout.flush();
        time.sleep(0.05)

    def loader(self, bar_progress_p, bar_empty_p, g_p, time_trans):
        time_init_loader = time.time()
        while True:
            for i in range(1,5):
                dict = {
                        1: self.bar('-', bar_progress_p, bar_empty_p, g_p,\
                                   time_trans + time.time() - time_init_loader),
                        2: self.bar('/', bar_progress_p, bar_empty_p, g_p,\
                                   time_trans + time.time() - time_init_loader),
                        3: self.bar('|', bar_progress_p, bar_empty_p, g_p,\
                                   time_trans + time.time() - time_init_loader),
                        4: self.bar('\\', bar_progress_p, bar_empty_p, g_p,\
                                   time_trans + time.time() - time_init_loader)
                        }


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-g', '--gain', nargs=2, type=int, required=True,\
                        help='apaala')
    args = parser.parse_args()
    time_gain = 18.0

    if args.gain[0] > args.gain[1]:
        i = -1
        gain_list = range(args.gain[0], args.gain[1] + i, i)
        try:
            time_init = time.time()
            m_bar_class = bar_class()
            for g in gain_list:
                bar_progress = ((args.gain[0]-g) * '#')
                bar_empty = ' ' * (g-args.gain[1])
                p = multiprocessing.Process(target=m_bar_class.loader,\
                                            args=(bar_progress, bar_empty, g,\
                                                 time.time() - time_init,))
                p.start()
                time.sleep(time_gain)
                p.terminate()
        except [[KeyboardInterrupt]]:
            pass 
        
        sys.stdout.write("\r[%s%s] Current Gain:%f / Time running: %0.3f \n"%\
                        ('#' * (args.gain[0]-args.gain[1]-i), ' ' * 0, g,\
                         time.time() - time_init))

    elif args.gain[0] < args.gain[1]:
        i = 1
        gain_list = range(args.gain[0], args.gain[1] + i, i)
        try:
            time_init=time.time()
            for g in gain_list:
                bar_progress = (g-args.gain[0]) * '#'
                bar_empty = ' ' * (args.gain[1]-g)
                p = multiprocessing.Process(target=m_bar_class.loader,\
                                            args=(bar_progress, bar_empty, g,\
                                                 time.time() - time_init,))
                p.start()
                time.sleep(time_gain)
                p.terminate()
        except [[KeyboardInterrupt]]:
            pass
        sys.stdout.write("\r[%s%s] Current Gain:%f / Time running: %0.3f \n"%\
                        ('#' * (args.gain[1]-args.gain[0] + i), ' ' * 0 , g,\
                        time.time() - time_init))

    else:
        print "The gain need to have different values"
        sys.exit()
    


        
