import multiprocessing as mp
from PIL import Image
import os, time



def video_converter(lis):  
    fpath, start, end = lis

    fdir, fname_fext = os.path.split(fpath)
    fdir_fname, fext = os.path.splitext(fpath)
    fname = fdir_fname.split('/')[-1] 

    if (fname_fext.endswith(start) and not os.path.exists( fdir_fname+end )):
        print(f"子處理程序ID:{os.getpid()} // ffmpeg -i {fname}{start} -vcodec h264 -acodec aac {fname}{end}")
        os.system(f"ffmpeg -i '{fdir_fname}{start}' -vcodec h264 -acodec aac '{fdir_fname}{end}'")  
        os.remove(fpath)         # delete after converted original file


def picture_converter(lis):  
    fpath, start, end = lis
    fdir, fname_fext = os.path.split(fpath)
    fdir_fname, fext = os.path.splitext(fpath)
    fname = fdir_fname.split('/')[-1] 
    if (fname_fext.endswith(start) and not os.path.exists( fdir_fname+end )):

        print(f"子處理程序ID:{os.getpid()} // PIL {fname}{start} -> {fname}{end}")
        img_png = Image.open(fpath, mode='r')
        rgb_img = img_png.convert('RGB')
        rgb_img.save( os.path.join(fdir, (fname+ end.lower())) )
        os.remove(fpath)          # delete after converted original file



def show(get_result):
    print(f'Callback: {get_result} PID: {os.getpid()}')


def del_duplicate(fpath, start, end):
    fdir_fname, fext = os.path.splitext(fpath)
    if os.path.exists(fdir_fname+start) and os.path.exists(fdir_fname+end):
        os.remove(fdir_fname+start)


if __name__ == '__main__':

    ss = time.time()

    print(f'cpu threads: {mp.cpu_count()}, 主處理程序 ID: {os.getpid()}')
    threads = mp.cpu_count() -2  # threads不排到滿 
    pool = mp.Pool( 4 )

    directory = os.getcwd() # assign directory

    video_thread_list = []
    pic_thread_list = []

    for fdir, dirs, files in os.walk(directory):
        for fname_fext in files:
            fpath = os.path.join(fdir, fname_fext)
            fdir_fname, fext = os.path.splitext(fpath)


            if fext.lower() in ['.mov', '.mp4']:
                video_thread_list.append((fpath, '.mov', '.mp4'))
                video_thread_list.append((fpath, '.MOV', '.MP4'))    

            elif fext.lower() in ['.png', '.jpg']:
                pic_thread_list.append((fpath, '.png', '.jpg'))
                pic_thread_list.append((fpath, '.PNG', '.JPG')) 
            else:
                pass       


    results = pool.map_async(video_converter, video_thread_list, callback=show)
    results = pool.map_async(picture_converter, pic_thread_list, callback=show)
    
    pool.close()
    pool.join()


    for fdir, dirs, files in os.walk(directory):
        for fname_fext in files:
            fpath = os.path.join(fdir, fname_fext)
            del_duplicate(fpath, '.mov', '.mp4')
            del_duplicate(fpath, '.MOV', '.MP4')
            del_duplicate(fpath, '.png', '.jpg')
            del_duplicate(fpath, '.PNG', '.JPG')


    print(f'time lasting: {time.time()-ss}')
