<?php 
    //echo "hello";
    for($i=1; $i < 2399999999; $i++) {
        if(strpos(md5($i, true), "'='")){
            echo("pw = $i<br>");
            echo("result = ".md5($i, true)."<br>");
            break;
        }
    }
?>