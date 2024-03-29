#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2022/06/07 15:46:13
@Author  :   pan 
@Email   :   pfclr1218@hotmail.com
@Version :   1.0
@Desc    :   None
'''


from views import PathHundle, PayRoll

Finance_Dict = {
    '1、计提管理工资社保公积金': {
        '借': {
            '管理费用-工资': 0,
            '管理费用-社保': 0,
            '管理费用-公积金': 0
        },
        '贷': {
            '应付职工薪酬-工资': 0,
            '应付职工薪酬=社保': 0,
            '应付职工薪酬-公积金': 0,
            '其他应付款-代扣社保': 0,
            '其他应付款-代扣公积金': 0,
            '应交税费-应交个人所得税': 0
        }
    },
    '2、计提销售工资社保公积金': {
        '借': {
            '销售费用-工资': 0,
            '销售费用-社保': 0,
            '销售费用-公积金': 0
        },
        '贷': {
            '应付职工薪酬-工资': 0,
            '应付职工薪酬=社保': 0,
            '应付职工薪酬-公积金': 0,
            '其他应付款-代扣社保': 0,
            '其他应付款-代扣公积金': 0,
            '应交税费-应交个人所得税': 0
        }
    }
}


def main():
    PH = PathHundle()
    PH.dir_mk_by_cus(r'/Users/pan/Documents/02-work/03-客户')
    
    PY = PayRoll('202205')
    paydata = PY.run_func()


if __name__ == '__main__':
    main()
