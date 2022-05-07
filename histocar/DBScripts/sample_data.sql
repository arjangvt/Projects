********************************************************************
Written by: Arjang Fahim
Version:    1.0.0
Created on: 11/2/2018
********************************************************************
     
    

INSERT INTO public.colors
(color, is_active, created_at, updated_at)
values
('blue', true, now(), now()),
('red', true, now(), now()),
('green', true, now(), now()),
('black', true, now(), now()),
('gray', true, now(), now()),
('white', true, now(), now()),
('gold', true, now(), now()),
('silver', true, now(), now())



INSERT INTO pulic.states
(state, is_active, created_at, updated_at)
values
('CA', true, now(), now()),
('NY', true, now(), now());

INSERT INTO public.cities
(state_id, city, is_active, created_at, updated_at)
values
(1, 'newport', true, now(), now()),
(1, 'irvine', true, now(), now());

INSERT INTO public.currencies
(currency, currency_symbol, is_active, created_at, updated_at)
VALUES('USD', '$', true, now(), now());

INSERT INTO public.zipcodes
(zipcode, city_id, is_active, created_at, updated_at)
values
('92603', 1, true, now(), now()),
('92625', 1, true, now(), now()),
('92603', 2, true, now(), now()),
('92606', 2, true, now(), now());


INSERT INTO public.vehicle_makes
(vehicle_make, is_active, created_at, updated_at)
values
('toyota', true, now(), now()),
('jaguar', true, now(), now()),
('tesla', true, now(), now());

INSERT INTO public.vehicle_models
(vehicle_make_id, model, is_active, created_at, updated_at)
values
(1, 'camry', true, now(), now()),
(2, 'xj', true, now(), now()),
(3, 'model s', true, now(), now());

INSERT INTO public.onlinecardealers
(dealer, website_url, is_active, created_at, updated_at)
VALUES('cars', 'http://cars.com', true, now(), now());

INSERT INTO public.urllists
(onlinecardealer_id, vehicle_make_id, vehicle_model_id, zipcode_id, url, is_active, created_at, updated_at)
VALUES
(1, 1, 1, '1', 'https://www.cars.com/for-sale/searchresults.action/?mdId=20800&mkId=20088&rd=99999&searchSource=QUICK_FORM&stkTypId=28881&zc=92603', true, now(), now()),
(2, 2, 1, 1, '1', 'https://www.autotrader.com/cars-for-sale/Toyota/Camry/Irvine+CA-92603?zip=92603&marketExtension=true&startYear=1981&endYear=2019&makeCodeList=TOYOTA&searchRadius=25&modelCodeList=CAMRY&sortBy=relevance&numRecords=25&firstRecord=0', true, now(), now());

INSERT INTO public.car_maps
(onlinecardealer_id, vehicle_model_id, vehicle_make_id, mapped_model_id, mapped_make_id, is_active, created_at, updated_at)
VALUES(1, 1, 1, 20800, 20088, true, now(), now());

INSERT INTO public.histocar_lists (vehicle_model_id,vehicle_make_id,zipcode_id,onlinecardealer_id,vin_number,price,mileage,color_id,currency_id,carcondition_id,seller_name,seller_address,seller_telnumber,seller_address_region,seller_address_locality,image_url,image_local_url,content_url,content_local_url,is_active,created_at,updated_at) VALUES 
(1,1,1,1,'4T1B61HKXJU500241',24744,0,2,1,0,'Bob Smith Toyota','3333 Foothill Blvd CA Glendale','(888) 675-7341','CA','Glendale','https://www.cstatic-images.com/phototab/in/fae12c23e36c963941112c70e9e07fd2.jpg','C://Users//Arjang//Desktop//Projects//Historide//HistoCar//histocar//LocalStorage//images//be8e899a-ec98-11e8-b44e-e4029b1d4a83.jpg','https://www.cars.com/for-sale/searchresults.action/?mdId=20800&mkId=20088&rd=99999&searchSource=QUICK_FORM&stkTypId=28881&zc=92603','C://Users//Arjang//Desktop//Projects//Historide//HistoCar//histocar//LocalStorage//html//searchresults.action.html',true,'2018-11-19 23:49:06.397','2018-11-19 23:49:06.397')
,(1,1,1,1,'4T1BF1FKXCU512380',9490,0,2,1,0,'Mankato Ford','1935 Madison Ave MN Mankato','(507) 201-4188','MN','Mankato','https://www.cstatic-images.com/phototab/in/054a6b02e0ed7c00fd61284cc0bef92f.jpg','C://Users//Arjang//Desktop//Projects//Historide//HistoCar//histocar//LocalStorage//images//beb852a8-ec98-11e8-8712-e4029b1d4a83.jpg','https://www.cars.com/for-sale/searchresults.action/?mdId=20800&mkId=20088&rd=99999&searchSource=QUICK_FORM&stkTypId=28881&zc=92603','C://Users//Arjang//Desktop//Projects//Historide//HistoCar//histocar//LocalStorage//html//searchresults.action.html',true,'2018-11-19 23:49:06.397','2018-11-19 23:49:06.397')
,(1,1,1,1,'4T1BF1FK6FU917043',16000,0,2,1,0,'Janesville Nissan','2627 Morse St WI Janesville','(608) 423-5415','WI','Janesville','https://www.cstatic-images.com/phototab/in/f0bffe4d4270634263633e7cd24f1665.jpg','C://Users//Arjang//Desktop//Projects//Historide//HistoCar//histocar//LocalStorage//images//bee41724-ec98-11e8-9516-e4029b1d4a83.jpg','https://www.cars.com/for-sale/searchresults.action/?mdId=20800&mkId=20088&rd=99999&searchSource=QUICK_FORM&stkTypId=28881&zc=92603','C://Users//Arjang//Desktop//Projects//Historide//HistoCar//histocar//LocalStorage//html//searchresults.action.html',true,'2018-11-19 23:49:06.397','2018-11-19 23:49:06.397')
,(1,1,1,1,'4T4BF3EK7BR157069',8549,0,3,1,0,'Kenosha Nissan','8050 120th Ave WI Kenosha','(262) 891-4395','WI','Kenosha','https://www.cstatic-images.com/phototab/in/f8d498ea4ee3448debc64e341b081878.jpg','C://Users//Arjang//Desktop//Projects//Historide//HistoCar//histocar//LocalStorage//images//bf09e914-ec98-11e8-95ee-e4029b1d4a83.jpg','https://www.cars.com/for-sale/searchresults.action/?mdId=20800&mkId=20088&rd=99999&searchSource=QUICK_FORM&stkTypId=28881&zc=92603','C://Users//Arjang//Desktop//Projects//Historide//HistoCar//histocar//LocalStorage//html//searchresults.action.html',true,'2018-11-19 23:49:06.397','2018-11-19 23:49:06.397')
,(1,1,1,1,'4T1BF1FK1GU238203',17497,0,3,1,0,'Braeger Ford','4201 S. 27th Street WI Milwaukee','(414) 455-6987','WI','Milwaukee','https://www.cstatic-images.com/phototab/in/49b86fa4642d4db218bf6692752c1d07.jpg','C://Users//Arjang//Desktop//Projects//Historide//HistoCar//histocar//LocalStorage//images//bf32c7cc-ec98-11e8-a937-e4029b1d4a83.jpg','https://www.cars.com/for-sale/searchresults.action/?mdId=20800&mkId=20088&rd=99999&searchSource=QUICK_FORM&stkTypId=28881&zc=92603','C://Users//Arjang//Desktop//Projects//Historide//HistoCar//histocar//LocalStorage//html//searchresults.action.html',true,'2018-11-19 23:49:06.397','2018-11-19 23:49:06.397')
,(1,1,1,1,'JTNB11HK8J3032823',19500,0,3,1,0,'Berman''s INFINITI of Merrillville','1794 81st Ave IN Merrillville','(219) 552-7024','IN','Merrillville','https://www.cstatic-images.com/phototab/in/75c605932f880f7d470662cf52e37080.jpg','C://Users//Arjang//Desktop//Projects//Historide//HistoCar//histocar//LocalStorage//images//bf5c1bb4-ec98-11e8-8911-e4029b1d4a83.jpg','https://www.cars.com/for-sale/searchresults.action/?mdId=20800&mkId=20088&rd=99999&searchSource=QUICK_FORM&stkTypId=28881&zc=92603','C://Users//Arjang//Desktop//Projects//Historide//HistoCar//histocar//LocalStorage//html//searchresults.action.html',true,'2018-11-19 23:49:06.397','2018-11-19 23:49:06.397')
,(1,1,1,1,'4T1BK1FKXEU548939',16036,0,5,1,0,'Tom Wood Toyota','6408 Crane Dr IN Whitestown','(888) 258-7628','IN','Whitestown','https://www.cstatic-images.com/phototab/in/dbd417312fcc502d864c4f1b90ca211a.jpg','C://Users//Arjang//Desktop//Projects//Historide//HistoCar//histocar//LocalStorage//images//bf848554-ec98-11e8-81f5-e4029b1d4a83.jpg','https://www.cars.com/for-sale/searchresults.action/?mdId=20800&mkId=20088&rd=99999&searchSource=QUICK_FORM&stkTypId=28881&zc=92603','C://Users//Arjang//Desktop//Projects//Historide//HistoCar//histocar//LocalStorage//html//searchresults.action.html',true,'2018-11-19 23:49:06.397','2018-11-19 23:49:06.397')
,(1,1,1,1,'4T1B11HK4JU560644',21497,0,5,1,0,'Dellen Chrysler Dodge Jeep RAM','2640 W Main St IN Greenfield','(317) 399-5365','IN','Greenfield','https://www.cstatic-images.com/phototab/in/827ad73cca64cf45cdd6e1c7e483d90a.jpg','C://Users//Arjang//Desktop//Projects//Historide//HistoCar//histocar//LocalStorage//images//bfaaf378-ec98-11e8-b1af-e4029b1d4a83.jpg','https://www.cars.com/for-sale/searchresults.action/?mdId=20800&mkId=20088&rd=99999&searchSource=QUICK_FORM&stkTypId=28881&zc=92603','C://Users//Arjang//Desktop//Projects//Historide//HistoCar//histocar//LocalStorage//html//searchresults.action.html',true,'2018-11-19 23:49:06.397','2018-11-19 23:49:06.397')
,(1,1,1,1,'4T4BF1FK1CR258385',9995,0,5,1,0,'INFINITI of Cincinnati','9857 Kings Auto Mall Rd OH Cincinnati','(513) 685-0023','OH','Cincinnati','https://www.cstatic-images.com/phototab/in/fb142fbb0ef1ea502256d1f21a1531c2.jpg','C://Users//Arjang//Desktop//Projects//Historide//HistoCar//histocar//LocalStorage//images//bfcec9ee-ec98-11e8-93b9-e4029b1d4a83.jpg','https://www.cars.com/for-sale/searchresults.action/?mdId=20800&mkId=20088&rd=99999&searchSource=QUICK_FORM&stkTypId=28881&zc=92603','C://Users//Arjang//Desktop//Projects//Historide//HistoCar//histocar//LocalStorage//html//searchresults.action.html',true,'2018-11-19 23:49:06.397','2018-11-19 23:49:06.397')
,(1,1,1,1,'JTNBK3EK3A3047842',6892,0,2,1,0,'Joseph Fiat of Cincinnati','9848 Waterstone Blvd. OH Cincinnati','(513) 716-1347','OH','Cincinnati','https://www.cstatic-images.com/phototab/in/76b7a70f81b6043df999e19e82ba8583.jpg','C://Users//Arjang//Desktop//Projects//Historide//HistoCar//histocar//LocalStorage//images//bff4c2e8-ec98-11e8-92b1-e4029b1d4a83.jpg','https://www.cars.com/for-sale/searchresults.action/?mdId=20800&mkId=20088&rd=99999&searchSource=QUICK_FORM&stkTypId=28881&zc=92603','C://Users//Arjang//Desktop//Projects//Historide//HistoCar//histocar//LocalStorage//html//searchresults.action.html',true,'2018-11-19 23:49:06.397','2018-11-19 23:49:06.397')
;
INSERT INTO public.histocar_lists (vehicle_model_id,vehicle_make_id,zipcode_id,onlinecardealer_id,vin_number,price,mileage,color_id,currency_id,carcondition_id,seller_name,seller_address,seller_telnumber,seller_address_region,seller_address_locality,image_url,image_local_url,content_url,content_local_url,is_active,created_at,updated_at) VALUES 
(1,1,1,1,'4T1BE46K18U204316',9898,0,1,1,0,'Mark Thomas Ford, Inc.','3098 OH-5 OH Cortland','(330) 282-8215','OH','Cortland','https://www.cstatic-images.com/phototab/in/0ef99cce81956c76b1501a299853ea15.jpg','C://Users//Arjang//Desktop//Projects//Historide//HistoCar//histocar//LocalStorage//images//c0187246-ec98-11e8-99b3-e4029b1d4a83.jpg','https://www.cars.com/for-sale/searchresults.action/?mdId=20800&mkId=20088&rd=99999&searchSource=QUICK_FORM&stkTypId=28881&zc=92603','C://Users//Arjang//Desktop//Projects//Historide//HistoCar//histocar//LocalStorage//html//searchresults.action.html',true,'2018-11-19 23:49:06.397','2018-11-19 23:49:06.397')
,(1,1,1,1,'4T1BE46K97U587257',6200,0,3,1,0,'Kenny Ross Nissan','22030 Perry Hwy PA Zelienople','(888) 291-3274','PA','Zelienople','https://www.cstatic-images.com/phototab/in/d03c4145ac3c2f46b68744ecf355d2cb.jpg','C://Users//Arjang//Desktop//Projects//Historide//HistoCar//histocar//LocalStorage//images//c0412a06-ec98-11e8-9a7f-e4029b1d4a83.jpg','https://www.cars.com/for-sale/searchresults.action/?mdId=20800&mkId=20088&rd=99999&searchSource=QUICK_FORM&stkTypId=28881&zc=92603','C://Users//Arjang//Desktop//Projects//Historide//HistoCar//histocar//LocalStorage//html//searchresults.action.html',true,'2018-11-19 23:49:06.397','2018-11-19 23:49:06.397')
,(1,1,1,1,'4T4BF1FK6ER373437',13577,0,3,1,0,'Cross Creek Subaru','497 N McPherson Church Rd NC Fayetteville','(910) 808-3091','NC','Fayetteville','https://www.cstatic-images.com/phototab/in/0eeb985c73738a5064e7afd358d187d3.jpg','C://Users//Arjang//Desktop//Projects//Historide//HistoCar//histocar//LocalStorage//images//c06acbf6-ec98-11e8-b547-e4029b1d4a83.jpg','https://www.cars.com/for-sale/searchresults.action/?mdId=20800&mkId=20088&rd=99999&searchSource=QUICK_FORM&stkTypId=28881&zc=92603','C://Users//Arjang//Desktop//Projects//Historide//HistoCar//histocar//LocalStorage//html//searchresults.action.html',true,'2018-11-19 23:49:06.397','2018-11-19 23:49:06.397')
,(1,1,1,1,'JTNB11HK4J3037727',20909,0,1,1,0,'Toyota of Batavia','3899 W Main Street Rd NY Batavia','(585) 300-4946','NY','Batavia','https://www.cstatic-images.com/phototab/in/931b75cc0210d8629c19c843f6963dd3.jpg','C://Users//Arjang//Desktop//Projects//Historide//HistoCar//histocar//LocalStorage//images//c090c4fe-ec98-11e8-a0b6-e4029b1d4a83.jpg','https://www.cars.com/for-sale/searchresults.action/?mdId=20800&mkId=20088&rd=99999&searchSource=QUICK_FORM&stkTypId=28881&zc=92603','C://Users//Arjang//Desktop//Projects//Historide//HistoCar//histocar//LocalStorage//html//searchresults.action.html',true,'2018-11-19 23:49:06.397','2018-11-19 23:49:06.397')
,(1,1,1,1,'JTNB11HK1J3038365',19400,0,1,1,0,'Toyota of Bowie','16700 Governor Bridge Rd MD Bowie','(301) 850-6123','MD','Bowie','https://www.cstatic-images.com/phototab/in/e8a476f6e99c7eca40f024fe3fd9836b.jpg','C://Users//Arjang//Desktop//Projects//Historide//HistoCar//histocar//LocalStorage//images//c0bc1468-ec98-11e8-bb9e-e4029b1d4a83.jpg','https://www.cars.com/for-sale/searchresults.action/?mdId=20800&mkId=20088&rd=99999&searchSource=QUICK_FORM&stkTypId=28881&zc=92603','C://Users//Arjang//Desktop//Projects//Historide//HistoCar//histocar//LocalStorage//html//searchresults.action.html',true,'2018-11-19 23:49:06.397','2018-11-19 23:49:06.397')
,(1,1,1,1,'4T1BF32K13U038661',5993,0,1,1,0,'Mahwah Honda','345 NJ-17 NJ Mahwah','(866) 570-2963','NJ','Mahwah','https://www.cstatic-images.com/phototab/in/b2114ffb805fa4f0968b4d1e78fff029.jpg','C://Users//Arjang//Desktop//Projects//Historide//HistoCar//histocar//LocalStorage//images//c0e47e00-ec98-11e8-879b-e4029b1d4a83.jpg','https://www.cars.com/for-sale/searchresults.action/?mdId=20800&mkId=20088&rd=99999&searchSource=QUICK_FORM&stkTypId=28881&zc=92603','C://Users//Arjang//Desktop//Projects//Historide//HistoCar//histocar//LocalStorage//html//searchresults.action.html',true,'2018-11-19 23:49:06.397','2018-11-19 23:49:06.397')
,(1,1,1,1,'4T1BF3EK6BU591753',9769,0,1,1,0,'Toyota of Greenwich','75 E Putnam Ave CT Cos Cob','(877) 651-8036','CT','Cos Cob','https://www.cstatic-images.com/phototab/in/54f71076abf588b9e10dc6e56f1a89d1.jpg','C://Users//Arjang//Desktop//Projects//Historide//HistoCar//histocar//LocalStorage//images//c10bfd6c-ec98-11e8-bea7-e4029b1d4a83.jpg','https://www.cars.com/for-sale/searchresults.action/?mdId=20800&mkId=20088&rd=99999&searchSource=QUICK_FORM&stkTypId=28881&zc=92603','C://Users//Arjang//Desktop//Projects//Historide//HistoCar//histocar//LocalStorage//html//searchresults.action.html',true,'2018-11-19 23:49:06.397','2018-11-19 23:49:06.397')
,(1,1,1,1,'4T1BZ1HK2JU015647',31999,0,5,1,0,'A1 Toyota','50 Amity Rd CT New Haven','(866) 482-7973','CT','New Haven','https://www.cstatic-images.com/phototab/in/88e7226e06b5143c51353d72c64895a3.jpg','C://Users//Arjang//Desktop//Projects//Historide//HistoCar//histocar//LocalStorage//images//c1492480-ec98-11e8-a22d-e4029b1d4a83.jpg','https://www.cars.com/for-sale/searchresults.action/?mdId=20800&mkId=20088&rd=99999&searchSource=QUICK_FORM&stkTypId=28881&zc=92603','C://Users//Arjang//Desktop//Projects//Historide//HistoCar//histocar//LocalStorage//html//searchresults.action.html',true,'2018-11-19 23:49:06.397','2018-11-19 23:49:06.397')
,(1,1,1,1,'4T1BF1FK2CU014643',9906,0,5,1,0,'Balise Kia West Springfield','603 Riverdale St MA West Springfield','(413) 241-8680','MA','West Springfield','https://www.cstatic-images.com/phototab/in/d75a6dc57df0a1a24c4a6abb629d2dce.jpg','C://Users//Arjang//Desktop//Projects//Historide//HistoCar//histocar//LocalStorage//images//c1729f76-ec98-11e8-8434-e4029b1d4a83.jpg','https://www.cars.com/for-sale/searchresults.action/?mdId=20800&mkId=20088&rd=99999&searchSource=QUICK_FORM&stkTypId=28881&zc=92603','C://Users//Arjang//Desktop//Projects//Historide//HistoCar//histocar//LocalStorage//html//searchresults.action.html',true,'2018-11-19 23:49:06.397','2018-11-19 23:49:06.397')
,(1,1,1,1,'4T4BF1FK6GR547154',10390,0,5,1,0,'McGee Toyota','860 Washington St MA Hanover','(888) 716-5490','MA','Hanover','https://www.cstatic-images.com/phototab/in/195eca17a99212dc635eb95e9d96367d.jpg','C://Users//Arjang//Desktop//Projects//Historide//HistoCar//histocar//LocalStorage//images//c19ae20a-ec98-11e8-9469-e4029b1d4a83.jpg','https://www.cars.com/for-sale/searchresults.action/?mdId=20800&mkId=20088&rd=99999&searchSource=QUICK_FORM&stkTypId=28881&zc=92603','C://Users//Arjang//Desktop//Projects//Historide//HistoCar//histocar//LocalStorage//html//searchresults.action.html',true,'2018-11-19 23:49:06.397','2018-11-19 23:49:06.397')
;

