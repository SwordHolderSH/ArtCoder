# ArtCoder: An End-to-end Method for Generating Scanning-robust Stylized QR Codes
A terrible PyTorch implementation of "***ArtCoder: An End-to-end Method for Generating Scanning-robust Stylized QR Codes***".

The paper "***ArtCoder: An End-to-end Method for Generating Scanning-robust Stylized QR Codes***" has been accepted by CVPR 2021. If the work or code is useful to you, please cite
```
@inproceedings{artcoderCVPR2021,
  title={ArtCoder: An End-to-end Method for Generating Scanning-robust Stylized QR Codes.},
  author={Hao Su, Jianwei Niu, Xuefeng Liu, Qingfeng Li, Ji Wan, Mingliang Xu, Tao Ren},
  booktitle={IEEE Conference on Computer Vision and Pattern Recognition},
  year={2021}
}
```

## abstract
Quick Response (QR) code is one of the most worldwide used two-dimensional codes. Traditional QR codes appear as random collections of black-and-white modules that lack visual semantics and aesthetic elements, which inspires the recent works to beautify the appearances of QR codes. However, these works adopt fixed generation algorithms and therefore can only generate QR codes with a pre-defined style. In this paper, combining the Neural Style Transfer technique, we propose a novel end-to-end method, named ArtCoder, to generate the stylized QR codes that are personalized, diverse, attractive, and scanning-robust.~To guarantee that the generated stylized QR codes are still scanning-robust, we propose a Sampling-Simulation layer, a module-based code loss, and a competition mechanism. The experimental results show that our stylized QR codes have high-quality in both the visual effect and the scanning-robustness, and they are able to support the real-world application.

## Results

<table  >
<tr>
<td rowspan="2">1.1</td>
<td>1.2</td>
<td>1.3</td></tr>
<tr>
<!--<td>2.1</td>-->
<td>2.2</td>
<td>2.3</td></tr>
<tr>
</table>



<table>
 <tr>
   <td>Style&Content</td>
   <td>Output</td> 
 </tr>
 



 
 
 
 
 <tr height="400" valign="middle">
   <td >
      <td><div align=center><img src="https://github.com/SwordHolderSH/ArtCoder/blob/main/style/texture1.1.jpg" width="290" /></td>
      <td><div align=center><img src="https://github.com/SwordHolderSH/ArtCoder/blob/main/content/boy.jpg" width="290" /></td>
   </td>
   <td>
      <div align=center><img src="https://github.com/SwordHolderSH/ArtCoder/blob/main/demos/output_84.jpg" width="350" />
   </td>
 </tr>
 
 
 
 

 </table>
  <p align="center"> **Table 1**</p>
