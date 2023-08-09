// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DonationContract {
    address public owner;
    uint public totalDonated;

    struct Donation {
        address donor;
        uint amount;
        uint timestamp;
    }

    Donation[] public donations;

    constructor() {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
        _;
    }

    function donate() external payable {
        require(msg.value > 0, "Donation amount must be greater than 0");
        
        Donation memory newDonation = Donation({
            donor: msg.sender,
            amount: msg.value,
            timestamp: block.timestamp
        });

        donations.push(newDonation);
        totalDonated += msg.value;
    }

    function getDonationCount() external view returns (uint) {
        return donations.length;
    }

    function getDonationDetails(uint index) external view returns (address donor, uint amount, uint timestamp) {
        require(index < donations.length, "Invalid donation index");
        Donation storage donation = donations[index];
        return (donation.donor, donation.amount, donation.timestamp);
    }

    function getTotalDonated() external view returns (uint) {
        return totalDonated;
    }

    function withdrawFunds() external onlyOwner {
        payable(owner).transfer(address(this).balance);
    }
}
