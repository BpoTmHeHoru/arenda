//SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;
pragma abicoder v2;

contract main {

    enum Roles { guest, user, admin, manager }
    enum Statuses { ne_sdaetsa, v_spiske, sdaetsa }
    enum Veref { not_veref, v_proverke, veref }

    struct user {
        string[3] _FIO;
        string Email;
        string Number;
        Roles Role;
    }

    struct house {
        address Owner;
        address Buyer;
        uint256 KDNumber;
        uint256 Area;
        uint256 UseArea;
        uint8 Rooms;
        uint256 Amount;
        uint8 MinMonth;
        uint8 MaxMonth;
        Statuses Status;
        Veref Verefication;
        uint256 id;
    }

    //$ Маппинги
    mapping (address => user) users;   
    mapping (address => house[]) arendUserHouse; // хаусы, которые будет арендовать юсер
    mapping (address => house[]) userHouse;      // хаусы, которые юсер выставляет для ареды  
    mapping (address => string) datareg;
    mapping (uint32 => address) managerID;
    
    //$ Массивы 
    house[] verefHouses;  // хаусы которые выставлены на продажу в аренду

    modifier isManager(uint32 id) {
        require(managerID[id] == msg.sender, "You are Manager!"); //Проверка на манагера
        require(users[msg.sender].Role == Roles.manager);
        _;
    }

    modifier isUser {
        require(users[msg.sender].Role == Roles.user, "You are not Registred!");
        _;
    }

    modifier isAdmin() {
        require(users[msg.sender].Role == Roles.admin);
        _;
    }

    //$ Функции  ФУНКЦИОНАЛ ЮЗЕРА
    function reg(string[3] memory _fio, string memory _email, string memory _number) public  {
        users[msg.sender] = user(_fio, _email, _number, Roles.user);
    }

    function auth(string memory _email, string memory _number) public view returns (user memory) {
        require(keccak256(bytes(_email)) == keccak256(bytes(users[msg.sender].Email)));
        require(keccak256(bytes(_number)) == keccak256(bytes(users[msg.sender].Number)));
        return users[msg.sender];
    }

    function addHouseInSystem(uint256 kdn, uint256 area, uint256 usearea, uint8 rooms, uint amount) public isUser {
        userHouse[msg.sender].push(house(msg.sender, address(0), kdn, area, usearea, rooms, amount, 0, 0, Statuses.ne_sdaetsa, Veref.v_proverke, 0));
    }

    function removeHouseInSystem() public isUser {
        userHouse[msg.sender].pop();
    }

            // Не работает, можно не тыкаться, всё остальное работает
    function arendHouse(uint id, uint minMounth) public {
        userHouse[verefHouses[id].Owner].push();
        userHouse[msg.sender][verefHouses[id].id].MinMonth = uint8(minMounth);
    }

    //$ функционал менеджера

    function VerefHouse(string memory _str, address _to, uint256 kdn, uint256 area, uint256 usearea, uint8 rooms, uint amount) public returns (string memory) {
        require(users[msg.sender].Role == Roles.manager);
        if(keccak256(bytes(_str)) == keccak256(bytes("yes"))) {
        verefHouses.push(house(_to, address(0), kdn, area, usearea, rooms, amount, 0, 0, Statuses.v_spiske, Veref.veref, verefHouses.length));
        removeHouseInSystem();
        }
        if(keccak256(bytes(_str)) == keccak256(bytes("no"))) {
            return " Your hous not verefication! ";
        }
    }

    //$ функционал администратора

    function addNewManager(address _addr, string memory data, uint32 id) public isAdmin {
        datareg[_addr] = data;
        managerID[id] = _addr;
        users[_addr].Role = Roles.manager;
    }
    
    function addNewAdmin(address _addr, string memory data) public isAdmin {
        datareg[_addr] = data;
        users[_addr].Role = Roles.admin;
    }

    function delAdminManager(address _addr) public isAdmin {
        users[_addr].Role = Roles.user;
    }


}   