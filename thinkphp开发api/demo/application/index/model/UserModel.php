<?php
/**
 * Created by PhpStorm.
 * User: txf
 * Date: 2019-04-05
 * Time: 20:53
 */

namespace app\index\model;
use think\Db;
use think\Log;
use think\Model;

class UserModel extends Model
{
    /**
     * 注册一个用户
     * @param $user_name
     * @param $pwd
     * @return int
     */
    public function reg_user($user_name, $pwd)
    {
//        高并发情况下需要redis锁
        $data = Db::table("user")->where('name', '=',$user_name)->find();
        if (empty($data)) {
            $uid = $this->create_uuid();
            $reg_data = array(
                "uid" => $uid,
                "reg_time" => date('Y-m-d H:i:s',time()),
                "name" => $user_name,
                "pwd" => $pwd
            );
            try {
                Db::table("user")->insert($reg_data);
            } catch (\Exception $e) {
                Log::write($e->getMessage());
                return 0;
            }
            return 1;
        }
        return 0;

    }
    function create_uuid($prefix = ""){    //可以指定前缀
        $str = md5(uniqid(mt_rand(), true));
        $uuid  = substr($str,0,8) . '-';
        $uuid .= substr($str,8,4) . '-';
        $uuid .= substr($str,12,4) . '-';
        $uuid .= substr($str,16,4) . '-';
        $uuid .= substr($str,20,12);
        return $prefix . $uuid;
    }
}