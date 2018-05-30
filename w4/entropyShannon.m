function val=entropyShannon(symprob,base)
  if nargin < 1
       error("usage: entropy(symbol_probability_list); computes entropy in base-2");
  elseif nargin < 2
       base=2;
  end
  val=0.0;

  #eliminate zeros from x.
  x=symprob(symprob > 0);

  val=-sum(log10(x).*x)/log10(base);
  return
end