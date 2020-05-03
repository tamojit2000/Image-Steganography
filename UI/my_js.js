



function goBack()
{
	window.history.back()
}



function preview_image(event)
{
	var reader=new FileReader();
	reader.onload=function()
	{
		var output=document.getElementById('output_image');
		output.src=reader.result;
	}
	reader.readAsDataURL(event.target.files[0]);
}
async function Encrypt_js()
{
	var data=document.getElementById("upload_text").value
	var name=document.getElementById("upload_name").value

	let output=await eel.Encrypt_python(data,name)();
	//alert(output);
	document.getElementById("upload_text").value=output;
}
async function Browse_js()
{
	let img=await eel.Browse_python()();
	//alert(img);
	if (img==""){
		img="Images/sample_img.jpg";
	}
	document.getElementById("output_image").src=img;
}
async function Decrypt_js()
{
	let data=await eel.Decrypt_python()();
	//alert(data);
	document.getElementById("upload_text").innerHTML=data;
}