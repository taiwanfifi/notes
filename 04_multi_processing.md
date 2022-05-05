



- Multi-threading (多執行緒/多線程)：
資料彼此傳遞簡單，因為多執行緒的 memory 之間是共用的，但也因此要避免會有 Race Condition 問題
適合需要 I/O 密集，像是爬蟲需要時間等待 request 回覆

> 使用`threading`模組，不用特別安裝即可使用，是 Python 標準函式庫裡面的模組。




- Async IO：
Coroutine (協程 / 微線程)
所謂 Coroutine 就是一個可以暫停將執行權讓給其他 Coroutine 或 Awaitables obj 的函數，等其執行完後再繼續執行，並可以多次的進行這樣的暫停與繼續。




【Python教學】淺談 Coroutine 協程使用方法
關於 Python Parallelism 的教學：


- Multi-processing (多處理程序/多進程)：
資料在彼此間傳遞變得更加複雜及花時間，因為一個 process 在作業系統的管理下是無法去存取別的 process 的 memory
適合需要 CPU 密集，像是迴圈計算
> 使用 `multiprocessing`模組，不用特別安裝即可使用，是 Python 標準函式庫裡面的模組。


【Python教學】淺談 Multi-processing 使用方法
【Python教學】淺談 Multi-processing pool 使用方法


---









一. 為什麼會有 GIL 的出現？  
避免在在執行 multiple threads 時，CPython memory 會有 thread-safe 的問題，所以在 Python Source Code 直譯成 bytecodes 時增加 GIL (Global Interpreter Lock) 的全域鎖。也就是說 GIL 可以用於確保在 Python 運行時僅運行一個 Thread 來保證 Thread-safe。

二. 切換 thread 的時機？  
當一個執行緒沒有直譯超過 1000 個 bytecode 指令 (Python 2)，或是超過 5 ms (Python 3.2後) 的時候，執行緒將會釋放 GIL 來讓其他執行緒使用。所以 GIL 保證的 Thread-safe 是 Bytecode 而不是 Python Code。


三. 什麼是 thread-safe？  
當多執行緒同時運行，並對同一資源進行讀寫操作的修改時，必須保證其執行緒與執行緒間不會發生衝突，和數據修改不會發生錯誤，稱為 thread-safe。

而了解了 thread 的切換時機和 thread-safe 後，如何避免執行緒執行到一半就被其他執行緒，就要討論原子操作。

四. 什麼是原子操作 (atomic operation)？  
同上面所述的 GIL 保證的 Thread-safe 是在 Bytecode 層而不是 Python Code。所以能確保的是每行 Bytecode 都會被運行完成，而多行 Bytecode 時則有被中斷切換執行緒的可能性。

1. 舉個例子：  
運行 sort() 函式
```py
import dis

this_is_list = []

def list_sort():
    this_is_list.sort()
    return ‘ok’

dis.dis(list_sort)
```

輸出結果：
```py
>>> 0 LOAD_GLOBAL      0 (this_is_list)
>>> 2 LOAD_METHOD      1 (sort)
>>> 4 CALL_METHOD      0
>>> 6 POP_TOP
```
所以 sort 本身是單一個 bytecode，這代表在執行完 sort 前是沒有機會被中斷而釋放 GIL 的。而這個概念就叫做原子操作 (atomic operation)，也就是 “原子是最小的、不可分割的最小個體” 的意義。

2. 再舉個例子：  
運行 append() 函式
```py
import dis

this_is_list = []


def list_append():
    this_is_list.append('text')
    return 'ok'

dis.dis(list_append)
```

輸出結果：
```py
0 LOAD_GLOBAL     0 (this_is_list)
2 LOAD_METHOD     1 (append)
4 LOAD_CONST      1 ('text')
6 CALL_METHOD     1
8 POP_TOP
```
可以看到 append 函式的輸出中，比剛剛運行 sort 還多了一行 bytecode (4 LOAD_CONST 1 (‘text’))，也就是說有可能在運行到一半時，就被中斷換其他執行緒運行，所以 append 函式就不是一個原子操作～

五. 非原子操作，如何避免 Race Condition  
如果是非原子操作 (atomic operation) 的情況下，threading 標準庫內有提供一些方式來防止 race condition 的發生。而 Lock 和 RLock 其中兩個基本工具。

- Lock：Lock 是一個像大廳通行證的對象。一次只有一個 thread 可以擁有 Lock。基本功能是 `.acquire（）`和 `.release（）`或使用 `with self._lock`
- RLock：避免 Deadlock 發生，它允許一個 thread 在調用 `.release（）`之前多次`.acquire（）`，也就是鎖中鎖的概念，可以遞迴的鎖。


### Concurrency Programming 






###  Async IO




- 為什麼需要 Concurrency
- Python 中實現 Concurrency 的方法
- 面對 I/O Bound 爬蟲問題選擇
    - 執行程序時間比較
    - 記憶體和 Load average 負載比較
        1. Multi-processing-pool (多處理程序池/多進程池)
        2. Multi-threading-pool (多線池/多執行緒池)
        3. Coroutine (協程/微線程)


### Concurrency
簡單來說 Concurrency Programming 就是能在同一時刻做兩件以上事情的能力，例如使用不同 CPU 分別運行程式來提高效率 ，或是當程式在等待執行結果時 (如等待 request 請求)，先執行其他程式函式 (Coroutine)，把浪費的 CPU 週期充分利用！

1. Concurrency 併發：Concurrency 的定義是指有同時處理多個任務的能力，也是廣義的並行。
2. Parallelism 並行：在同一時間執行多個操作，而 Multi-processing 是一種實現並行性的方法。









