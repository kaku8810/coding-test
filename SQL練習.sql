insert into 都道府県
values ('37','四国','香川','高松',1876)

insert into 都道府県
(コード,都道府県名,県庁所在地)
values ('40','福岡','福岡')

update 都道府県
set 県庁所在地='京都'
where コード='26'

update 都道府県
set 地域='九州', 面積=4976
where コード='40'

delete from 都道府県
where コード='26'

select * from 家計簿
where メモ like '%1月%'