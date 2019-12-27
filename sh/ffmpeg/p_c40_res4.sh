for idx in `seq -f '%02g' 1 10`
do
{
  for vpath in `cat data$idx`
  do
    echo $vpath
    array=(${vpath//\// }) 
    echo ${array[0]} ${array[1]} ${array[2]}
    subpath=${array[1]}
    vname=${array[2]}
  
    savepath=c40
    if [ ! -d "${savepath}/${subpath}" ];then
      echo "${savepath}/${subpath}" "not exist"
    mkdir  "${savepath}/${subpath}" 
    fi
    ffmpeg -i $vpath -crf 40 ${savepath}/${subpath}/$vname
  
    savepath=res4
    if [ ! -d "${savepath}/${subpath}" ];then
      echo "${savepath}/${subpath}" "not exist"
    mkdir  "${savepath}/${subpath}" 
    fi
    ffmpeg -i $vpath -vf scale=iw*0.25:ih*0.25 ${savepath}/${subpath}/$vname
  
  done
}&
done
