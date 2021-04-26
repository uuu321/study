class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 用来保存结果
        res = ""
        # 循环zip生成的元组列表
        for tmp in zip(*strs):
            # set是将zip中的元组转化为集合（自动去重）
            tmp_set = set(tmp)
            # 如果len(tmp_set)大于1说明不属于公共前缀，因为转换为set自动去重后长度为1说明是共有的
            if len(tmp_set) == 1:
                # 连接赋值给res
                res += tmp[0]
            # 只要出现一个不是共有的，后面的就不用考虑
            else:
                break
        return res