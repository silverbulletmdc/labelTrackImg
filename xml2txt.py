import untangle
import os

def xml_to_txt(xml_dir, txt_filepath, classnames_path = None, use_one_class = False):
    '''
    将VOC格式的xml标注转化为txt文件。
    :param xml_dir:
    :param txt_filepath:
    :param use_one_class: 如果为true，则将所有的类别都认为是一种。
    
    :return:
    '''
    labels = []
    frames = []

    for filename in os.listdir(xml_dir):
        if filename[-3:] != 'xml':
            continue 
        frames.append(filename)
    frames = sorted(frames)

    for filename in frames:    
        annotation = untangle.parse(os.path.join(xml_dir, filename)).annotation
        # print(filename)
        for object in annotation.object:
            try:
                data = {}
                data['filename'] = annotation.filename.cdata
                data['class'] = object.name.cdata
                # data['width'] = int(annotation.size.width.cdata)
                # data['height'] = int(annotation.size.height.cdata)
                data['xmin'] = int(object.bndbox.xmin.cdata)
                data['ymin'] = int(object.bndbox.ymin.cdata)
                data['xmax'] = int(object.bndbox.xmax.cdata)
                data['ymax'] = int(object.bndbox.ymax.cdata)
                data['width'] = data['xmax'] - data['xmin']
                data['height'] = data['ymax'] - data['ymin']
                labels.append(data)
            except:
                pass

    with open(txt_filepath, 'w') as f:
        for label in labels:
            line = '{},{},{},{}\n'.format(
                # label['filename'],
                label['xmin'],
                label['ymin'],
                label['width'],
                label['height'],
                # 1 if use_one_class else class_name2index[label['class']]
            )
            f.write(line)

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        print('please input the vidoes file path')
        quit()

    for root, dir, files in os.walk(path):
        for item in dir:
            print('process video:', item)    
            labels_dir = os.path.join(root, item)
            xml_to_txt(labels_dir, os.path.join(root, item+'.txt'), use_one_class=True)
