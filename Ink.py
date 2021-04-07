import numpy as np

class Ink:
    """ This code is designed for calculating the amount of materials required for specific ink. """

    # 输入格式 solvent = [[溶剂1的体积，溶剂1的密度],[溶剂2的体积，溶剂2的密度], ......]
    # 单位为[mL, g/cm**3]
    def __init__(self,solvent):
        self.num_solvent = len(solvent)
        self.V_solvent = []
        self.P_solvent = []
        self.M_solvent = []
        for n in range(len(solvent)):
            self.V_solvent.append(solvent[n][0])
            self.P_solvent.append(solvent[n][1])
            self.M_solvent.append(solvent[n][0]*solvent[n][1])

    def Unit(self,unit):
        unit_dict = {'g':1.0,'mg':1000.0,'ug':1000000.0}
        return unit_dict[unit]

    # 输入格式 mass_fraction = [溶质1的质量百分浓度,溶质2的质量百分浓度, ......]
    # 单位为 wt%
    def GetSoluteMass(self,mass_fraction,unit='g'):
        m_solvent = sum(self.M_solvent)  # Calculating the total mass of the solvent
        num_solute = len(mass_fraction)
        mass_fraction = [mass_fraction[i]*0.01 for i in range(num_solute)]  # 调整单位，化为百分比
        sigma = [1.0]*num_solute
        mass_fraction_tensor = np.array([[mass_fraction[j]*sigma[i] for i in range(num_solute)] for j in range(num_solute)])
        identity = np.identity(num_solute)  # 生成以溶质数目为维数的单位矩阵
        A = identity-mass_fraction_tensor
        b = np.array([mass_fraction[i]*m_solvent for i in range(num_solute)])
        x = np.linalg.solve(A,b)  # 解向量方程：Ax=b, A是矩阵，x跟b是向量
        return x*self.Unit(unit)


if __name__ == '__main__':
    ink = Ink([[20,0.945]])
    print(ink.GetSoluteMass([5.0],'mg'))