### ToC

- [Express](#express)
- [RESTful](#restful)
    - [HTTP Request](#httprequest)
    - [REST傳輸要求](#rest傳輸要求)
    - [API安全性](#api安全性)
    - [URI命名](#url命名)
- [Javascript](#javascript)
    - [使用習慣](#使用習慣)
    - [Array陣列](#array陣列)
    - [Object物件](#object物件)
    - [Assignment](#assignment)




### Express 
---
> Node.js 底下的一個前端 + 後端的框架，包含 MVC Framework( Model–View–Controller)  
View 就是前端畫面呈現 HTML + CSS  
Model、Controller 為後端 API 搭建資料庫與控制流程   


```
┌── app.js
├── bin
│   └── www  // 程式進入點
├── package-lock.json
├── package.json
├── public
│   ├── images
│   ├── javascripts
│   └── stylesheets
│       └── style.css
├── routes  // 路由
│   ├── index.js
│   └── users.js
└── views
    ├── error.jade
    ├── index.jade
    └── layout.jade

```

bin/www 是整個程式的進入點，點進去你可以發現他的 port 設為 3000 代表 web server 監聽埠號 3000 port  
其他相關的 middleware 例如：body-parser、morgan 以及 router 都寫在 app.js 中被 www 啟動時所 import 進去  
前端畫面是 public 與 views 這兩個資料夾管理  

- 解析 routes/index.js  
`/test` 路徑並傳送文字 `router.get` 是代表建立一個路由並使用 HTTP request methods 中的 get 形式，HTTP request methods 定義非常多個請求方式。
`router.get`中有兩個參數，第一個是子路徑名稱用單引號字串包起來，第二個是一個方法裡面面有三個參數分別為 req(request)接收資料、res(respond)回傳資料以及next。  

    ```javascript
    // index.js
    var express = require('express');
    var router = express.Router();

    /* GET home page. localhost:3000/ */
    router.get('/', function(req, res, next) {
    res.render('index', { title: 'Express' });
    });

    /* GET localhost:3000/test */
    router.get('/test', function(req, res, next) {
    res.send('This is localhost:3000/test')
    });

    module.exports = router;
    ```

- 執行  
修改檔案後就可以使用 `node ./bin/www` 或 `npm start` 來啟動專案，至於後者指令為什麼可以啟動，你可以查看 package.json 的檔案裡面的 scripts 有設定好指令相對路徑，所以在 package.json 中你可以依據你的習慣設定你自己專屬的快捷鍵。

    ```javascript
    // 兩者選一都能啟動程式
    node ./bin/www
    npm start
    ```


### RESTful  
---
Representational State Transfer，簡稱 REST，它是一種網路架構風格，近幾年來 REST 的概念已經被實作在大型網路系統中，而在 Web Service 中使用 REST 概念被實作出來的 API 就簡稱為 RESTful API 他是使用 HTTP 的協定完整定義 Web Service 在 HTTP Request 的各種流程。

#### HTTPRequest
HTTP 本身就是 REST 的實作，所謂的 HTTP Request 定義了八種請求方法分別為：

- GET  
此方法只能向指定的資源要求取得資料，並不會更動到內部資源  
- HEAD  
HEAD 跟 GET 方法類似只差別在它並不會回傳你所請求的資源在 body 上，只回傳 HTTP header  
- POST  
向指定的資源提交資料  
- PUT  
向指定資源位置提交更新內容  
- DELETE  
向指定資源位置請求刪除內容  
- CONNECT  
HTTP/1.1協議中預留給能夠將連接改為管道方式的代理服務器  
- OPTIONS  
此方法可使服務器傳回該資源所支持的所有 HTTP 請求方法  
- TRACE  
回顯服務器收到的請求，主要用於測試或診斷  


#### REST傳輸要求 

REST 風格最重要的架構約束有六個:

1. 客戶-服務器（Client-Server） - 客戶端和服務器結構
2. 無狀態（Stateless） - 連接協議具有無狀態性
3. 緩存（Cache） - 能夠利用Cache機制增進性能
4. 統一接口（Uniform Interface）- 一致性的操作界面
5. 分層系統（Layered System） - 層次化的系統
6. 按需代碼（Code-On-Demand，可選） - 例如 JavaScript

#### API安全性
RESTful 設計 API 時，保證 RESTful API 的安全性，PUT 或 DELETE 其實並不安全，在沒有權限認證下任何人都可以存取此方法。

基本流程如下：  
會員機制(帳號密碼) -> 服務端驗證成功並取得一組 API token -> 使用此組 token 訪問 API 資源


#### URI命名
RESTful API 的 URI 命名
> URL root: https://example/api/  
建議 URI components 都用小寫  
URI 使用名詞而不是動詞，且建議使用複數  

- BAD
    ```
    /getProducts
    /listOrders
    /getProductsById?orderId=1
    ```

- GOOD
    ```
    GET => /products (回傳所有產品)
    POST => /products (新增產品)
    GET => /products/4 (取得單筆產品)
    PUT => /products/4 (修改單筆筆產品)
    DELETE => /products/4 (刪除單筆產品)
    ```

- MVC 一種軟體架構模式    
把系統分成 Model, View, Controller  
    > Web 中分別:  
    前端 HTML+CSS (View) - 前端畫面與邏輯顯示  
    後端 API 資料庫(Model) - 後端資料庫進行運作   
    控制後端資料庫的接口 JavaScript (Controller) - 處理控制流程和回應，以路由以傳遞資料為主 


### JavaScript  
---
#### 使用習慣

1. 宣告 let  
使用 let 聲明的變量，其作用域為該語句所在的代碼塊內，使用時機例如: 陳述句(if、else)、迴圈(for)  
    ```javascript
    for (let i = 0; i < 10; i += 1) {
    console.log('loop is run ${i} times');
    }
    console.log(i); // ReferenceError: i is not defined
    ```

2. 宣告 const  
使用 const 聲明的是常量，在後面出現的代碼中不能再修改該常量的值。使用時機例如:不會變動的值  
    ```javascript
    const mName = 'Andy Tsai';
    mName = 'Tsai Andy'; // TypeError: Assignment to constant variable.
    console.log(mName);
    ```

3. 大量的if、esle if、else 
會造成程式冗長與不易閱讀，所以這時就可以使用 switch 判斷也可以達到相同效果。
    ```javascript
    switch (expression) {
    case value1:
        //符合時執行語句
        break;
    case value2:
        //符合時執行語句
        break;
    ...
    default:
        //以上都無則進入此區域
        break;n
    }
    ```


4. 使用i+=1 而非i++做每次間隔，由於官方 ESLint 建議Unary operator '++' used. (no-plusplus) 不要使用 ++ -- 
    ```javascript
    for (let i = 0 ; i < 10 ; i +=1){
        console.log(i);
    }
    ```

5. 迭代取值
- `for of`   
是 ES6 新增的語句，可用於迭代就件上取出容器裡的值例如陣列、Map、Set、字串等等。  
    ```javascript
    let mArray = [1, 2, 3]
    for (let value of mArray) {
    console.log(value); // 1 2 3
    }
    ```

- `foEach`
    ```javascript
    const numbers = [1, 2, 3, 4, 5];
    let sum = 0;
    numbers.forEach(num => sum += num);
    console.log(sum) // 15
    ```

6. 函式(function)  
函式 (function) 又稱方法 (method)，用於程式碼過多重複時定義一個方法來去重複呼叫  
箭頭函式在 JavaScript 中改寫原本 function 的撰寫方式。較短的語法外，在保持this 關鍵字範圍方面也有優勢  
    ```javascript
    // 使用有名稱的函式
    function sum(a, b){
        return a+b;
    }
    // 常數指定為匿名函式
    const sum = function(a, b) {
        return a+b;
    }
    // 箭頭函式
    const sum = (x, y) => {
    return x + y;
    };
    console.log(sum(1, 3)); 
    ```

7. 撰寫方式
    1. 當你在宣告時若沒有傳入值(arguments)，必須放空括號。
        ```javascript
        const callMe = () => { 
        console.log('Max!');
        }
        ```
    2. 當只有一個傳入值(arguments)，可以省略括號。
        ```javascript
        const callMe = name => { 
            console.log(name);
        }
        ```
    3. 當函式有回傳時可濃縮一行
        ```javascript
        const doubleNum = num => num * 2;

        console.log(doubleNum(5));
        ```
        等同
        ```javascript
        const doubleNum = (num) => {
        return num * 2;
        };
        console.log(doubleNum(5));
        ```


#### Array陣列  

- 陣列初始化
    - 立即給值
        ```js
        const arr = [1, 2, 3]
        console.log(arr.length) // 3
        ```        
    - 後續給值
        ```js
        const arr = []
        arr[0] = 1
        arr[1] = 2
        arr[2] = 3
        console.log(arr.length) // 3
        ```

- 展開(spread)運算子
展開運算值是 ES6 的一個新的特性，可以使用 `...` 代表陣列，用函式來做示範，當不知道引數有多少時可以很方便使用。
    ```js
    const call = (...arr) => {
    console.log(arr); // [ 1, 2, 3 ]
    };
    call(1, 2, 3); 
    ```

#### Object物件  
- 物件是儲存資料最常見的一種型態，主要是以一個鍵 (key) 搭配一個值 (value):
    ```js
    const dog = {
        name: 'Tom',
        breed: 'Golden Retriever',
        weight: 60
        }
    ```

- 存取物件內的值  
有兩種方法分別如下，第一種是利用 物件名稱.key 拿取值，第二種方法是利用陣列回傳方式 物件名稱[key] 取得相對應內容。  
    ```js
    console.log(dog.breed) // Golden Retriever
    console.log(dog["breed"]) // Golden Retriever
    ```

- 物件使用 forEach 方法  
陣列的 forEach 方法，雖然 for...in 也可以，但 ESLint 並不推薦

    ```js
    const dog = {
        name: 'Tom',
        breed: 'Golden Retriever',
        weight: 60
        };
        Object.keys(dog).forEach((key) => {
        console.log(dog[key]);
        });

    Output：
            // Tom
            // Golden Retriever
            // 60
    ```

- 物件夾帶方法  
在物件中不僅可以儲存值，方法也行，可以想作 function 存在一個變數中。

    ```js
    const dog = {
        name: 'Tom',
        breed: 'Golden Retriever',
        weight: 60,
        breaks() {
            console.log('woof'); 
        }
        };
    dog.breaks(); // woof
    ```

- Spread & Rest Operators  
符號都是三個點(...)
    - 在陣列值運算  
    一個是展開陣列中的值，一個是集合其餘的值成為陣列  
    - 展開運算子(Spread Operator)    
    Used to split up array element or object poperties  
    簡單來說像是陣列與物件的變數繼承  

    ```js
    // 陣列展開用法
    const numbers = [1, 2, 3];
    const newNumbers = [...numbers, 4];

    console.log(newNumbers);
    //output: [1, 2, 3, 4]
    ```

    ```js
    // 物件展開用法
    const person = {
    name: 'Andy',
    };
    const newPerson = {
    ...person,
    age: 21,
    };

    console.log(newPerson);
    //output: { name: 'Andy', age: 21 }
    ```

    - 其餘運算符(Rest Operator)  
    Used to merge a list of function arguments into an array  
    雖然與展開運算子特性的符號是一模一樣的，都是三個點(...)，但使用的情況與意義不同  
    Array.filter()方法會過濾陣列的元素，並將通過測試的元素傳回成為一個新陣列。  
    Array.filter()方法使用回呼函式來對元素進行過濾，須由設計師自行撰寫過濾程式。  

    ```js
    // Array.filter() 過濾陣列元素
    const filter = (...args) => args.filter(el => el === 2);

    console.log(filter(1, 2, 3));
    //output: [ 2 ]
    ```

#### Assignment
- Destructuring Assignment (解構賦值)  
Easily extract array elements or object properties and store them in variables  
解構解構允許你拉出單個元素或屬性，並將他們儲存在數組的變數中  

    - Array Destructuring  

    ```js
    const numbers = [1, 2, 3];
    const [num1, num2] = numbers;

    console.log(num1, num2);
    //output: 1 2
    ```

- Reference and Primitive Types  
    - 變數參數傳值(passed by value)  

    ```js
    let num1 = 1;
    const num2 = num1;
    num1 = 2;

    console.log(num1, num2);
    //output: 2 1
    ```

- 物件傳址(passed by reference)

    ```js
    const person = {
    name: 'Andy'
    };
    const secondPerson = person;
    person.name = 'Tank';

    console.log(secondPerson);
    //output: { name: 'Tank' }
    ```

- 此方法為複製屬性而不是整個物件

    ```js
    const person = {
    name: 'Andy'
    };
    const secondPerson = {
    ...person
    };

    person.name = 'Tank';
    console.log(secondPerson);
    //output: { name: 'Andy' }
    ```


