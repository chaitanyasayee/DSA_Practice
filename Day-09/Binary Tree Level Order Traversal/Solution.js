var levelOrder = function(root) {
    if (!root) return [];

    const ans = [];
    const queue = [root];

    while (queue.length > 0) {
        const level = [];
        const n = queue.length;

        for (let i = 0; i < n; i++) {
            const node = queue.shift();
            level.push(node.val);

            if (node.left) queue.push(node.left);
            if (node.right) queue.push(node.right);
        }

        ans.push(level);
    }

    return ans;
};