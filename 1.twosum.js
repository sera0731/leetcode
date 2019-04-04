/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    
    let map = new Map();
    
    for (let i=0, max=nums.length; i<max; i++){
        
        const diff = target-nums[i];
        
        if (map.has(diff)){
            return [map.get(diff), i];
        }
        
        map.set(nums[i], i);
        
    }
    
    return ans;
    
};