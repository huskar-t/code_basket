<?php
/**
 * Created by PhpStorm.
 * User: txf
 * Date: 2019-04-05
 * Time: 20:54
 */

namespace app\index\controller;
use app\index\model\UserModel;

class User{
    public function reg(){
        $post_data = file_get_contents('php://input');
        $json_data = json_decode($post_data,true);
        $user_name = $json_data['name'];
        $password = $json_data['pwd'];
        $um = new UserModel();
        $result = $um->reg_user($user_name,$password);
        if($result == 1){
            return "success";
        }else{
            return "fail";
        }
    }
}