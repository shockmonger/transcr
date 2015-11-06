import numpy as np




                var reader = new FileReader();
                reader.onload = function (e) {
                    var contents = e.target.result;
                    var x = contents.replace(/\n/g, " ");
                    x = x.split(" ");
                    displayContents("aa");
                    var i;
                    var time = [], freq = [];
                    var count = 0;
                    var j = 0;
                    var k = 0;
                    var ratios = [1 / 1, 17 / 16, 9 / 8, 19 / 16, 5 / 4, 21 / 16, 11 / 8, 3 / 2, 13 / 8, 27 / 16, 7 / 4, 15 / 8];
                    var names = ["s", "r1", "r2", "g1", "g2", "m1", "m2", "p", "d1", "d2", "n1", "n2"];
                    var base = 466.164;
                    for (i = 0; i < ratios.length; i++)
                    {
                        ratios[i] = ratios[i] * base;
                        console.log(ratios[i]);
                    }

                    for (i = 6; i < x.length; i++)
                    {
                        displayContents(x[i]);
                        if (x[i] !== '')
                        {
                            displayContents(x[i] + "AAA");
                            if (count % 2 !== 0)
                            {
                                time[j] = x[i];
                                j++;
                                count++;
                            }
                            else
                            {
                                if (x[i] == "--undefined--")
                                {
                                    freq[k] = parseFloat("0", 10);
                                }
                                else
                                {
                                    freq[k] = parseFloat(x[i], 10);
                                }
                                k++;
                                count++;
                            }

                        }


                    }
                    displayContents(freq[0] + "   " + freq[1]);
                    var t1 = 5;
                    avg = [];
                    for (i = 0; i < 1000; i++)
                    {
                        avg[j] = 0;
                    }
                    cnt = [];
                    var j = 0;
                    var flag = 0;
                    var min = [], max = [], prev;
                    for (i = 0; i < freq.length; i++)
                    {

                        if (flag === 0 && freq[i] !== 0)
                        {


                            flag = 1;
                            cnt[j] = 1;
                            min[j] = freq[i];
                            max[j] = freq[i];
                            avg[j] = freq[i];

                        }
                        else if (Math.abs(freq[i] - min[j]) < t1 && Math.abs(freq[i] - max[j] < t1) && freq[i] !== 0)
                        {

                            cnt[j]++;
                            avg[j] += freq[i];
                            if (freq[i] < min[j])
                            {
                                min[j] = freq[i];
                            }
                            else if (freq[i] > max[j])
                            {
                                max[j] = freq[i];
                            }

                        }
                        else
                        {


                            if (freq[i] !== 0)
                            {
                                flag = 0;
                                j++;
                                cnt[j] = 1;
                                min[j] = freq[i];
                                max[j] = freq[i];
                                avg[j] = freq[i];
                            }
                        }
                    }
                    var t2 = 10;
                    var check = [];
                    for (var k = 0; k < j; k++)
                    {
                        check[k] = k;
                    }
                    for (k = 0; k < j - 1; k++)
                    {
                        if (cnt[k] > 1)
                            avg[k] = avg[k] / cnt[k];
                        else
                            avg[k] = 0;
                        console.log(min[k] + "\t" + max[k] + "\t" + avg[k] + "\n");
                        if (Math.abs(min[k] - min[k + 1]) < t2 && Math.abs(max[k] - max[k + 1]) < t2)
                        {
                            check[k + 1] = check[k]
                        }
                    }

                    var results = [];
                    for (i = 0; i < j; i++)
                    {
                        results[j] = -1;
                    }
                    var l = 0;
                    for (k = 0; k < j; k++)
                    {
                        if (avg[k] !== 0)
                        {
                            l = 0;
                            var diff1 = 1111, diff2 = 1111;
                            while (avg[k] > ratios[l])
                            {
                                diff1 = Math.abs(avg[k] - ratios[l])
                                l++;

                            }
                            diff2 = Math.abs(avg[k] - ratios[l]);
                            if (diff1 < diff2)
                                results[k] = l - 1;
                            else
                                results[k] = l;
                            console.log("dffff" + "   " + diff1 + "  " + diff2 + "   " + results[k]);
                        }
                        else
                            continue;

                    }


                    //   displayContents(min[0]+"dd"+max[0]+"DDD"+j+"ff");
                    // displayContents("aa"+min);
                    // displayContents("bb"+avg);

                };
                reader.readAsText(file);
            }

