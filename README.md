# labelTrackImg
This is a useful tool to label temporal sequence images based on [labelImg](https://github.com/tzutalin/labelImg) project.

I change a little code of labelImg to fit the tracking label task.

The changes could summarized by following:
- Tracking object will not offset from last image huge. So when you click next img, the scale and offsets of the canvas will be remained. So that you can label the image continuously.
- The position of image could be predict by interpolating its neighboring image. when you click next image, The next bndbox would predict automatically by interpolated the last two images. So you can just finetune the bndbox.
## Quick start

I use python3.6 and pyqt5 to develop. Execute the following command to configure project.
```
pip install pyqt5
pyrcc5 -o resources.py resources.qrc
```
Execute the following command to start project.
```shell
python labelImg.py
```
补充:缺啥少啥就pip install啥

PS: lack what less what then you pip install what

For more details, you can read the [original repo](https://github.com/tzutalin/labelImg).
