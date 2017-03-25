CREATE TABLE `area` (
   `small_area_name` varchar(50),
   `pref_name` varchar(25),
   `coupon_id_hash` varchar(32)
	) ENGINE=MyISAM; 

CREATE TABLE `detail` (
   `item_count` tinyint unsigned,
   `i_date` datetime,
   `small_area_name` varchar(50),
   `purchaseid_hash` varchar(32),
   `user_id_hash` varchar(32),
   `coupon_id_hash` varchar(32)
	) ENGINE=MyISAM;

CREATE TABLE `list` (
    `capsule_text` varchar(21),
    `genre_name` varchar(24),
    `price_rate` tinyint unsigned,
    `catalog_price` mediumint unsigned,
    `discount_price` mediumint unsigned,
    `dispfrom` datetime,
    `dispend` datetime,
    `dispperiod` tinyint unsigned,
    `validfrom` date,
    `validend` date,
    `validperiod` tinyint unsigned,
    `usable_date_mon` tinyint unsigned,
    `usable_date_tue` tinyint unsigned,
    `usable_date_wed` tinyint unsigned,
    `usable_date_thu` tinyint unsigned,
    `usable_date_fri` tinyint unsigned,
    `usable_date_sat` tinyint unsigned,
    `usable_date_sun` tinyint unsigned,
    `usable_date_holiday` tinyint unsigned,
    `usable_date_before_holiday` tinyint unsigned,
    `large_area_name` varchar(14),
    `ken_name` varchar(20),
    `small_area_name` varchar(41),
    `coupon_id_hash` varchar(32)
    ) ENGINE=MyISAM;

CREATE TABLE `visit` (
    `PURCHASE_FLG` tinyint(1),
    `I_DATE` datetime,
    `PAGE_SERIAL` smallint unsigned,
    `REFERRER_hash` varchar(32),
    `VIEW_COUPON_ID_hash` varchar(32),
    `USER_ID_hash` varchar(32),
    `SESSION_ID_hash` varchar(32),
    `PURCHASEID_hash` varchar(32)
    ) ENGINE=MyISAM;

CREATE TABLE `user` (
        `reg_date` datetime,
        `sex_id` varchar(1),
        `age` tinyint unsigned,
        `withdraw_date` datetime,
        `pref_name` varchar(20),
        `user_id_hash` varchar(32)
    ) ENGINE=MyISAM;