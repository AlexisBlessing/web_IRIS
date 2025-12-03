Get-ChildItem *.png | ForEach-Object { 
	& "C:\Users\Alexis\Downloads\libwebp-1.6.0-windows-x64\libwebp-1.6.0-windows-x64\bin\cwebp.exe" 
	-q 80 $_.FullName -o ($_.BaseName + ".webp")
}


Get-ChildItem *.png | ForEach-Object {
    	$output = "$($_.BaseName).webp"
    	& "C:\Users\Alexis\Downloads\libwebp-1.6.0-windows-x64\libwebp-1.6.0-windows-x64\bin\cwebp.exe" -q 80 $_.FullName -o $output
}