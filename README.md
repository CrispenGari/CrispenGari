### 𝐇𝐞𝐥𝐥𝐨 𝐭𝐡𝐞𝐫𝐞 !

_an undergraduate computer science **(dropout)** student who's interested in learning more about technology. infinity love for **c**omputer **v**ision **(cv)** and **n**atural **l**anguage **p**rocessing **(nlp)** using ai/deep learning._

[@crispengari](https://crispengari-ac2c8.web.app/) _**deep learning enthusiast.**_

```c++
#include "CMakeProject2.h"
#include <torch/torch.h>
using namespace std;

int main(){
  torch::Tensor tensor = torch::eye(3);
  cout << tensor << endl;
  return 0;
}
```

What i want to learn this year.

1. [x] _koa.js_
2. [x] _django_
3. [ ] _reinforcement learning **(rl)**_
4. [x] _java springboot_
5. [ ] _machine learning in C++_
6. [ ] _robotics_
7. [ ] _docker_
8. [x] _prisma_
9. [x] _urql_
10. [ ] _java swing(awt)_
11. [ ] _game engine in javascript_
12. [x] _electron.js_
13. [ ] _svelte.js_
14. [ ] _vs-code extentions_
15. [ ] _react component library_
16. [ ] _aws_
17. [ ] _kubernetes_
I'm so fascinated with deep learning using `torch` look how clean is this code.

```py
class LeNet(nn.Module):
    def __init__(self, output_dim):
        super(LeNet, self).__init__()
        self.features = nn.Sequential(
            nn.Conv2d(in_channels=1, out_channels=6, kernel_size =5),
            nn.MaxPool2d(kernel_size=2),
            nn.ReLU(),
            nn.Conv2d(in_channels=6, out_channels=16, kernel_size =5),
            nn.MaxPool2d(kernel_size=2),
            nn.ReLU()
        )
        self.classifier = nn.Sequential(
            nn.Linear(16 * 4 * 4, 120),
            nn.ReLU(),
            nn.Linear(120, 84),
            nn.ReLU(),
            nn.Linear(84, output_dim)
        )

    def forward(self, x):
        x = self.features(x) # x = [batch size, 16, 4, 4]
        x = x.view(x.shape[0], -1) # x = [batch size, 16*4*4 = 256]
        x = self.classifier(x) # x = [batch size, output dim]
        return x
```


<p align="center">
<a href="https://www.linkedin.com/in/crispen-gari-34437720b" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-%230077B5.svg?&style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
<a href="https://www.instagram.com/crispen_gari_/" target="_blank"><img src="https://img.shields.io/badge/Instagram-%23E4405F.svg?&style=flat-square&logo=instagram&logoColor=white" alt="Instagram"></a>
<a href="https://www.facebook.com/crispen.gari" target="_blank"><img src="https://img.shields.io/badge/Facebook-%231877F2.svg?&style=flat-square&logo=facebook&logoColor=white" alt="Facebook"></a>
</p>
