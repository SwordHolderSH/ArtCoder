# ArtCoder: An End-to-end Method for Generating Scanning-robust Stylized QR Codes
A PyTorch implementation of "***ArtCoder: An End-to-end Method for Generating Scanning-robust Stylized QR Codes***".

The paper "***ArtCoder: An End-to-end Method for Generating Scanning-robust Stylized QR Codes***" has been accepted by CVPR 2021. If the paper or code is useful for your research, please cite
```
@inproceedings{su2021artcoder,
  title={ArtCoder: An End-to-End Method for Generating Scanning-Robust Stylized QR Codes},
  author={Su, Hao and Niu, Jianwei and Liu, Xuefeng and Li, Qingfeng and Wan, Ji and Xu, Mingliang and Ren, Tao},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  pages={2277--2286},
  year={2021}
}
```

## Demos

<table>
  
<tr>
   <td align="center">Style&Content</td>
   <td align="center">Output</td> 
</tr>
 
<tr>
 <td height="250" width="280" align="center"><div align=center><img src="https://github.com/SwordHolderSH/ArtCoder/blob/main/style/texture1.1.jpg" width="230" /></td>
 <td rowspan="2" align="center" width="550" height="550"><img src="https://github.com/SwordHolderSH/ArtCoder/blob/main/demos/output_84.jpg" width="500" /></td>
</tr>
<tr height="250">
  <td align="center" width="280"><div align=center><div align=center><img src="https://github.com/SwordHolderSH/ArtCoder/blob/main/content/boy.jpg" width="230" /></td> 
</tr>

<tr>
 <td height="250" width="280" align="center"><div align=center><img src="https://github.com/SwordHolderSH/ArtCoder/blob/main/style/s55v2.jpg" width="230" /></td>
 <td rowspan="2" align="center" width="550" height="550"><img src="https://github.com/SwordHolderSH/ArtCoder/blob/main/demos/output_105.jpg" width="500" /></td>
</tr>
<tr height="250">
  <td align="center" width="280"><div align=center><div align=center><img src="https://github.com/SwordHolderSH/ArtCoder/blob/main/content/boy.jpg" width="230" /></td> 
</tr>
    
 <tr>
 <td height="250" width="280" align="center"><div align=center><img src="https://github.com/SwordHolderSH/ArtCoder/blob/main/style/s6.jpg" width="230" /></td>
 <td rowspan="2" align="center" width="550" height="550"><img src="https://github.com/SwordHolderSH/ArtCoder/blob/main/demos/output_170.jpg" width="500" /></td>
</tr>
<tr height="250">
  <td align="center" width="280"><div align=center><div align=center><img src="https://github.com/SwordHolderSH/ArtCoder/blob/main/content/boy.jpg" width="230" /></td> 
</tr>
    
 <tr>
 <td height="250" width="280" align="center"><div align=center><img src="https://github.com/SwordHolderSH/ArtCoder/blob/main/style/paper-cut.jpg" width="180" /></td>
 <td rowspan="2" align="center" width="550" height="550"><img src="https://github.com/SwordHolderSH/ArtCoder/blob/main/demos/output_290.jpg" width="500" /></td>
</tr>
<tr height="250">
  <td align="center" width="280"><div align=center><div align=center><img src="https://github.com/SwordHolderSH/ArtCoder/blob/main/content/ship.jpg" width="230" /></td> 
</tr>  
 
 <tr>
 <td height="250" width="280" align="center"><div align=center><img src="https://github.com/SwordHolderSH/ArtCoder/blob/main/style/s45.2.jpg" width="230" /></td>
 <td rowspan="2" align="center" width="550" height="550"><img src="https://github.com/SwordHolderSH/ArtCoder/blob/main/demos/output_78.jpg" width="500" /></td>
</tr>
<tr height="250">
  <td align="center" width="280"><div align=center><div align=center><img src="https://github.com/SwordHolderSH/ArtCoder/blob/main/content/dog.jpg" width="230" /></td> 
</tr>
    
 <tr>
 <td height="250" width="280" align="center"><div align=center><img src="https://github.com/SwordHolderSH/ArtCoder/blob/main/style/redwave4.jpg" width="230" /></td>
 <td rowspan="2" align="center" width="550" height="550"><img src="https://github.com/SwordHolderSH/ArtCoder/blob/main/demos/output_182.jpg" width="500" /></td>
</tr>
<tr height="250">
  <td align="center" width="280"><div align=center><div align=center><img src="https://github.com/SwordHolderSH/ArtCoder/blob/main/content/ca.jpg" width="230" /></td> 
</tr>
    
<tr>
 <td height="250" width="280" align="center"><div align=center><img src="https://github.com/SwordHolderSH/ArtCoder/blob/main/style/s6.jpg" width="230" /></td>
 <td rowspan="2" align="center" width="550" height="550"><img src="https://github.com/SwordHolderSH/ArtCoder/blob/main/demos/output_375.jpg" width="500" /></td>
</tr>
<tr height="250">
  <td align="center" width="280"><div align=center><div align=center><img src="https://github.com/SwordHolderSH/ArtCoder/blob/main/content/ca.jpg" width="230" /></td> 
</tr>
    
<tr>
 <td height="250" width="280" align="center"><div align=center><img src="https://github.com/SwordHolderSH/ArtCoder/blob/main/style/texture1.1.jpg" width="230" /></td>
 <td rowspan="2" align="center" width="550" height="550"><img src="https://github.com/SwordHolderSH/ArtCoder/blob/main/demos/output_66.jpg" width="500" /></td>
</tr>
<tr height="250">
  <td align="center" width="280"><div align=center><div align=center><img src="https://github.com/SwordHolderSH/ArtCoder/blob/main/content/brad.jpg" width="230" /></td> 
</tr>

<tr>
 <td height="250" width="280" align="center"><div align=center><img src="https://github.com/SwordHolderSH/ArtCoder/blob/main/style/picasso_selfport1907.jpg" width="230" /></td>
 <td rowspan="2" align="center" width="550" height="550"><img src="https://github.com/SwordHolderSH/ArtCoder/blob/main/demos/brad.jpg" width="500" /></td>
</tr>
<tr height="250">
  <td align="center" width="280"><div align=center><div align=center><img src="https://github.com/SwordHolderSH/ArtCoder/blob/main/content/brad.jpg" width="230" /></td> 
</tr>

<tr>
 <td height="250" width="280" align="center"><div align=center><img src="https://github.com/SwordHolderSH/ArtCoder/blob/main/style/s41.2.jpg" width="230" /></td>
 <td rowspan="2" align="center" width="550" height="550"><img src="https://github.com/SwordHolderSH/ArtCoder/blob/main/demos/output_131.jpg" width="500" /></td>
</tr>
<tr height="250">
  <td align="center" width="280"><div align=center><div align=center><img src="https://github.com/SwordHolderSH/ArtCoder/blob/main/content/man.jpg" width="230" /></td> 
</tr>
 
 <tr>
 <td height="250" width="280" align="center"><div align=center><img src="https://github.com/SwordHolderSH/ArtCoder/blob/main/style/texture1.1.jpg" width="230" /></td>
 <td rowspan="2" align="center" width="550" height="550"><img src="https://github.com/SwordHolderSH/ArtCoder/blob/main/demos/output_68.jpg" width="500" /></td>
</tr>
<tr height="250">
  <td align="center" width="280"><div align=center><div align=center><img src="https://github.com/SwordHolderSH/ArtCoder/blob/main/content/man.jpg" width="230" /></td> 
</tr>

<tr>
 <td height="250" width="280" align="center"><div align=center><img src="https://github.com/SwordHolderSH/ArtCoder/blob/main/style/candy.jpg" width="230" /></td>
 <td rowspan="2" align="center" width="550" height="550"><img src="https://github.com/SwordHolderSH/ArtCoder/blob/main/demos/output_147.jpg" width="500" /></td>
</tr>
<tr height="250">
  <td align="center" width="280"><div align=center><div align=center><img src="https://github.com/SwordHolderSH/ArtCoder/blob/main/content/love.jpg" width="230" /></td> 
</tr>
    
<tr>
 <td height="250" width="280" align="center"><div align=center><img src="https://github.com/SwordHolderSH/ArtCoder/blob/main/style/candy.jpg" width="230" /></td>
 <td rowspan="2" align="center" width="550" height="550"><img src="https://github.com/SwordHolderSH/ArtCoder/blob/main/demos/output_295.jpg" width="500" /></td>
</tr>
<tr height="250">
  <td align="center" width="280"><div align=center><div align=center><img src="https://github.com/SwordHolderSH/ArtCoder/blob/main/content/panda.jpg" width="230" /></td> 
</tr>

</table>

## Prerequisites
 
 * Linux or Windows
 * CPU or NVIDIA GPU + CUDA CuDNN
 * Python 3
 * Pytorch 1.7.0

## Getting Started

### Installation

* Clone this repo:
```
    git clone https://github.com/SwordHolderSH/ArtCoder
    cd ArtCoder
```
* Install PyTorch and other dependencies.

### Quick Start
* Get detailed information about all parameters using
```
    python main.py -h
```

* Generate your customized Stylized QR codes:
```
    python main.py -style_img_path ./xxxx/xxx.jpg  --content_img_path ./xxxx/xxx.jpg --code_img_path ./xxxx/xxx.jpg --output_dir ./xxxx/
```
### Notices
* The input code images are generated by the algorithm on the website https://meiyaoma.com/ . Of course, it is OK to use traditional QR codes (square modules appear as random distribution) as the input code images, and it just compromises some visual quality.
<table>
<tr height="200">
 <td    align="center"><div align=center><img src="https://github.com/SwordHolderSH/ArtCoder/blob/main/code/boy.jpg" width="200" /></td>
  <td   align="center"><div align=center><img src="https://github.com/SwordHolderSH/ArtCoder/blob/main/code/ca.jpg" width="200" /></td>
    <td    align="center"><div align=center><img src="https://github.com/SwordHolderSH/ArtCoder/blob/main/code/brad.jpg" width="200" /></td>
      <td    align="center"><div align=center><img src="https://github.com/SwordHolderSH/ArtCoder/blob/main/code/city.jpg" width="200" /></td>
         <td    align="center"><div align=center><img src="https://github.com/SwordHolderSH/ArtCoder/blob/main/code/dog.jpg" width="200" /></td>
</tr>
</table>

* The QR codes of version 5 is used by default ```(37*37 modules)```. If you want to use different versions of QR code, you need to adjust the parameters ```--module_number (default: 37)```.
