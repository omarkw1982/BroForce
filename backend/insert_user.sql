INSERT INTO `BroForce`.`Users`
(`userid`,
`name`,
`role`,
`password`,
`time_created`,
`status`)
VALUES
(UUID(),
'yusuf',
'doctor',
SHA1('sharingan'),
NOW(),
'active');
