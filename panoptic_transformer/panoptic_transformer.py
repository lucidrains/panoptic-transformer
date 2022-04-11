import torch
from torch import nn, einsum
from einops import rearrange
import torch.nn.functional as F

class Attention(nn.Module):
    def __init__(
        self,
        dim,
        *,
        dim_head = 64,
        heads = 8
    ):
        super().__init__()
        inner_dim = heads * dim_head
        self.scale = dim_head ** -0.5
        self.heads = heads

        self.to_q = nn.Linear(dim, inner_dim, bias = False)
        self.to_kv = nn.Linear(dim, dim_head * 2, bias = False)
        self.to_out = nn.Linear(inner_dim, dim, bias = False)

    def forward(self, x):
        q, k, v = (self.to_q(x), *self.to_kv(x).chunk(2, dim = -1))

        q = rearrange(q, 'b n (h d) -> b h n d', h = self.heads)
        q = q * self.scale

        sim = einsum('b h i d, b j d -> b h i j', q, k)

        attn = sim.softmax(dim = -1)

        out = einsum('b h i j, b j d -> b h i d', attn , v)

        out = rearrange(out, 'b h n d -> b n (h d)')
        return self.to_out(out)


class PanopticTransformer(nn.Module):
    def __init__(
        self,
        dim,
        dim_head = 64,
        heads = 8
    ):
        super().__init__()

    def forward(self, x):
        return x
