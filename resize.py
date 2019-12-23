import os,sys
import cv2
import argparse
from tqdm import tqdm
def myResize(saveRoot, readRoot, lists, resize_width, resize_heigh):
  with open(readRoot + lists,'r') as fp:
    lines = fp.readlines() 
    print("total:", len(lines))
    for line in tqdm(lines):
      subpath = line.strip().split(' ')[0]
      path = readRoot + '/' + subpath
      img = cv2.imread(path)
      try:
        img.shape
      except:
        print(path, "not exist!")
      nimg = cv2.resize(img, (resize_width, resize_heigh) )
      dirlist = subpath.split('/')
      subdir = ''
      for dirs in dirlist[:-1]:
        subdir = subdir + '/' + dirs
      if not os.path.isdir(saveRoot + '/' + subdir):
        os.makedirs(saveRoot + '/' + subpath)
      #nsubpath = subpath.replace( '.jpg', '_w%d_h%d.jpg'%(resize_width, resize_heigh) )
      cv2.imwrite(saveRoot + subpath, nimg)
    
if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('--listfile', type=str, default='lst')
  parser.add_argument('--inRoot', type=str, default='./')
  parser.add_argument('--rW', type=int, default=112) 
  parser.add_argument('--rH', type=int, default=112) 
  parser.add_argument('--saveRoot', type=str, default='./112/')
  args = parser.parse_args()
  print(args)
  
  myResize(args.saveRoot, args.inRoot, args.listfile, args.rW, args.rH)
