import torch

def linear_regression_normal_equation(X, y) -> torch.Tensor:
    """
    Solve linear regression via the normal equation using PyTorch.
    X: Tensor or convertible of shape (m,n); y: shape (m,) or (m,1).
    Returns a 1-D tensor of length n, rounded to 4 decimals.
    """
    X_t = torch.as_tensor(X, dtype=torch.float)
    y_t = torch.as_tensor(y, dtype=torch.float).reshape(-1, 1)

    XT = X_t.T
    A = XT @ X_t
    theta = torch.linalg.pinv(A) @ XT @ y_t  # stable normal equation
    theta = theta.view(-1)
    theta = torch.round(theta * 10000) / 10000
    return theta