pragma solidity ^0.4.0;
contract BikeRegistry {

    struct BikeRegister {
        string code; // service code, e.g. 1001/FOO/BAR
        string serialno; // long string
        uint count;
        bool recorded;
    }

    event Record(bytes32 hash, string serialno, uint count);

    function record(bytes32 hash, string code, string serialno, uint count) external {
        require(registry[hash].recorded);
        registry[hash] = BikeRegister(code, serialno, count, true);
    }

    mapping (bytes32 => BikeRegister) public registry;
}
