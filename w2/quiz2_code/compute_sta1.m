function [ sta ] = compute_sta1( stim_list, spike_train)
    %First run generate_spiketrain_from_linear_filter
%Then run compute_sta 

spike_indices = find(spike_train==1);
numspikes=length(spike_indices);

sta_length=250;  %choose a number less than or equal to filter_length so have enough of stim defined
sta=zeros(1,sta_length);

for j=1:numspikes
    sta=sta+stim_list(spike_indices(j)-sta_length: spike_indices(j)-1 );
end

sta = sta/numspikes;  %normalize
  
  
end
  