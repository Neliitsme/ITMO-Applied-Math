import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


class Solve:
    def __init__(
            self,
            flow_intensity=7.23,
            service_intensity=4.9,
            channel_count=4,
            queue_size=1,
    ):
        self.alpha = flow_intensity
        self.mu = service_intensity
        self.r = channel_count
        self.m = queue_size

        self.s = [0 for _ in range(1 + self.r + self.m)]
        self.s[0] = 1

        self.t = np.linspace(0, 2)

    def generate_step(self):
        if len(self.s) == 1:
            return lambda s, t: s

        def step(s, t):
            ans = [0 for _ in range(len(s))]
            for i in range(len(s)):
                if i < len(s) - 1:
                    ans[i] -= self.alpha * s[i]
                    ans[i] += min(self.r, i + 1) * self.mu * s[i + 1]
                if i > 0:
                    ans[i] += self.alpha * s[i - 1]
                    ans[i] -= min(self.r, i) * self.mu * s[i]
            return ans
        return step

    def draw(self, data: np.matrix):
        for i in range(data.shape[1]):
            plt.plot(self.t, data[:, i])
        plt.show()

    def transform_to_avg(self, steps: np.matrix):
        ans = []
        for step in steps:
            ans.append([0, 0])
            for i in range(step.shape[1]):
                ans[-1][0] += min(self.r, i) * step[0, i]
                ans[-1][1] += max(self.r - i, 0) * step[0, i]

        print(ans)
        ans = np.matrix(ans)
        return ans

    def solve(self):
        func = self.generate_step()

        steps = odeint(func, self.s, self.t)
        steps = np.matrix(steps)
        self.draw(steps)

        avg_steps = self.transform_to_avg(steps)
        self.draw(avg_steps)


if __name__ == "__main__":
    kebab2 = Solve()
    kebab2.solve()
